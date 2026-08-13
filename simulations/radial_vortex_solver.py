"""Radial vortex BVP solver for the coupled-field vortex model.

Model (dimensionless):
  L = -1/4 F^2 + |D psi|^2 + 1/2 (dX)^2 - V
  V = a|psi|^2 + b|psi|^4 + c|psi|^2 X^2 - 1/2 X^2 + 1/4 X^4

Axisymmetric ansatz:
  psi = f(r) exp(i n phi)
  A = A_phi(r) e_phi
  X = X(r)

The script solves n=1,2,3 sectors and reports E_n - n E_1.
"""
from __future__ import annotations

import argparse
import numpy as np
from scipy.integrate import solve_bvp, simpson
from scipy.optimize import brentq


def mixed_vacuum(a: float, b: float, c: float) -> tuple[float, float]:
    D = b - c*c
    if D <= 0:
        raise ValueError("mixed branch requires b-c^2>0")
    rho = -(a + c) / (2.0 * D)
    x2 = (b + a*c) / D
    if rho <= 0 or x2 <= 0:
        raise ValueError("parameters are outside the mixed-vacuum region")
    return float(np.sqrt(rho)), float(np.sqrt(x2))


def solve_vortex(a: float, b: float, c: float, q: float, n: int,
                 radius: float = 22.0, points: int = 500, tol: float = 1e-5):
    f0, x0 = mixed_vacuum(a, b, c)
    r = np.linspace(1e-5, radius, points)
    f = f0*np.tanh(r)
    x = x0 + (1.0-x0)*np.exp(-r)
    A = (n/q)*(1.0-np.exp(-r*r))/(r+1e-12)
    y = np.vstack([f, np.gradient(f,r), x, np.gradient(x,r), A, np.gradient(A,r)])

    def ode(rr, yy):
        f, fp, x, xp, A, Ap = yy
        inv = 1.0/rr
        ang = n*inv - q*A
        fpp = -inv*fp + ang*ang*f + (a + 2*b*f*f + c*x*x)*f
        xpp = -inv*xp + (-1.0 + x*x + 2*c*f*f)*x
        App = -inv*Ap + A*inv*inv - 2*q*f*f*(n*inv-q*A)
        return np.vstack([fp, fpp, xp, xpp, Ap, App])

    def bc(ya, yb):
        return np.array([ya[0], ya[3], ya[4], yb[0]-f0, yb[2]-x0, yb[4]-n/(q*radius)])

    sol = solve_bvp(ode, bc, r, y, tol=tol, max_nodes=20000)
    if sol.status != 0:
        raise RuntimeError(sol.message)
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
