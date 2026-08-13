"""Radial vortex BVP solver for the coupled-field vortex model.

Model (dimensionless):
  L = -1/4 F^2 + |D psi|^2 + 1/2 (dX)^2 - V
  V = a|psi|^2 + b|psi|^4 + c|psi|^2 X^2 - 1/2 X^2 + 1/4 X^4

Axisymmetric ansatz:
  psi = f(r) exp(i n phi)
  A = A_phi(r) e_phi
  X = X(r)
"""
from __future__ import annotations

import argparse
import numpy as np
from scipy.integrate import solve_bvp, simpson


def mixed_vacuum(a: float, b: float, c: float) -> tuple[float, float]:
    D = b - c*c
    if D <= 0:
        raise ValueError("mixed branch requires b-c^2>0")
    rho = -(a + c) / (2.0 * D)
    x2 = (b + a*c) / D
    if rho <= 0 or x2 <= 0:
        raise ValueError("parameters are outside the mixed-vacuum region")
    return float(np.sqrt(rho)), float(np.sqrt(x2))


def _solve_once(a: float, b: float, c: float, q: float, n: int,
                radius: float, points: int, tol: float,
                initial_solution=None, initial_n: int | None = None,
                max_nodes: int = 120000):
    f0, x0 = mixed_vacuum(a, b, c)
    r = np.linspace(1e-5, radius, points)

    if initial_solution is None:
        # Bag-informed profile is substantially more robust for large winding.
        D = b-c*c
        dV = (a+c)**2/(4*D)
        Rb = np.sqrt(np.sqrt(2.0)*n/(q*np.sqrt(dV))) if dV > 0 else np.sqrt(n)
        s = .5*(1+np.tanh((r-Rb)/1.5))
        f = f0*s
        x = 1.0 + (x0-1.0)*s
        A = (n/q)*(1.0-np.exp(-(r/max(Rb,1e-6))**2))/(r+1e-12)
        y = np.vstack([f, np.gradient(f,r), x, np.gradient(x,r), A, np.gradient(A,r)])
    else:
        y = initial_solution.sol(r).copy()
        if initial_n is not None and initial_n != n:
            scale = n/initial_n
            y[4] *= scale
            y[5] *= scale

    def ode(rr, yy):
        f, fp, x, xp, A, Ap = yy
        inv = 1.0/rr
        ang = n*inv - q*A
        fpp = -inv*fp + ang*ang*f + (a + 2*b*f*f + c*x*x)*f
        xpp = -inv*xp + (-1.0 + x*x + 2*c*f*f)*x
        App = -inv*Ap + A*inv*inv - 2*q*f*f*(n*inv-q*A)
        return np.vstack([fp, fpp, xp, xpp, Ap, App])

    def bc(ya, yb):
        return np.array([ya[0], ya[3], ya[4],
                         yb[0]-f0, yb[2]-x0, yb[4]-n/(q*radius)])

    sol = solve_bvp(ode, bc, r, y, tol=tol, max_nodes=max_nodes)
    if sol.status != 0:
        raise RuntimeError(sol.message)
    return sol


def _continuation_ladder(n: int) -> list[int]:
    if n <= 8:
        return [n]
    ladder = [1,2,4,8]
    step = 4 if n <= 40 else 8
    k = 12
    while k < n:
        ladder.append(k)
        k += step
    if ladder[-1] != n:
        ladder.append(n)
    return sorted(set(x for x in ladder if x <= n))


def solve_vortex(a: float, b: float, c: float, q: float, n: int,
                 radius: float = 22.0, points: int = 500, tol: float = 1e-5,
                 initial_solution=None, initial_n: int | None = None,
                 use_continuation: bool = True, max_nodes: int = 120000):
    """Solve one axisymmetric vortex sector.

    For high winding, the default path uses continuation in n.  This changes
    only the numerical initial guess, not the equations, boundary conditions,
    action, or convergence tolerance.  Callers may pass an existing solution
    explicitly for continuation in q or n.
    """
    if initial_solution is not None or not use_continuation or n <= 8:
        return _solve_once(a,b,c,q,n,radius,points,tol,
                           initial_solution,initial_n,max_nodes)

    sol = None
    prev_n = None
    for k in _continuation_ladder(n):
        sol = _solve_once(a,b,c,q,k,radius,points,tol,sol,prev_n,max_nodes)
        prev_n = k
    return sol


def vortex_energy(sol, a: float, b: float, c: float, q: float, n: int,
                  radius: float = 22.0, integration_points: int = 5000) -> float:
    f0, x0 = mixed_vacuum(a, b, c)
    r = np.linspace(1e-5, radius, integration_points)
    f, fp, x, xp, A, Ap = sol.sol(r)
    B = Ap + A/r
    V = a*f*f + b*f**4 + c*f*f*x*x - 0.5*x*x + 0.25*x**4
    V0 = a*f0*f0 + b*f0**4 + c*f0*f0*x0*x0 - 0.5*x0*x0 + 0.25*x0**4
    density = fp**2 + f*f*(n/r-q*A)**2 + 0.5*xp**2 + 0.5*B**2 + (V-V0)
    return float(2*np.pi*simpson(r*density, x=r))


def sector_energies(q: float, a=-0.8, b=1.0, c=0.4, radius=22.0, points=500):
    energies=[]
    for n in (1,2,3):
        sol=solve_vortex(a,b,c,q,n,radius,points)
        energies.append(vortex_energy(sol,a,b,c,q,n,radius))
    e1,e2,e3=energies
    return e1,e2,e3,e2-2*e1,e3-3*e1


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--q", type=float, nargs="*", default=[1.25,1.27,1.28,1.29,1.30])
    p.add_argument("--a", type=float, default=-0.8)
    p.add_argument("--b", type=float, default=1.0)
    p.add_argument("--c", type=float, default=0.4)
    p.add_argument("--radius", type=float, default=22.0)
    p.add_argument("--points", type=int, default=500)
    args=p.parse_args()
    print("q,E1,E2,E3,Delta2,Delta3")
    for q in args.q:
        vals=sector_energies(q,args.a,args.b,args.c,args.radius,args.points)
        print(f"{q:.8f},"+",".join(f"{v:.12g}" for v in vals))

if __name__ == "__main__":
    main()
