"""Large-winding (vortex-bag) approximation for the coupled-field vortex model.

For a large winding n, approximate the vortex as a circular core of radius R in the
psi=0, X=1 phase, surrounded by the mixed vacuum. The leading energy is

    E(R) = pi*DeltaV*R^2 + 2*pi*n^2/(q^2*R^2) + 2*pi*sigma*R + ...

The wall term is subleading as n->infinity. Minimizing the leading terms gives

    R_n^2 = sqrt(2)*n/(q*sqrt(DeltaV))
    E_n/n -> 2*pi*sqrt(2*DeltaV)/q.

The asymptotic fusion boundary is estimated by equating this limiting energy per
flux quantum to the numerically computed n=1 vortex energy E1(q).
"""
from __future__ import annotations

import argparse
import numpy as np
from scipy.optimize import brentq

from radial_vortex_solver import mixed_vacuum, solve_vortex, vortex_energy


def vacuum_energy(a: float, b: float, c: float) -> float:
    f0, x0 = mixed_vacuum(a, b, c)
    return a*f0*f0 + b*f0**4 + c*f0*f0*x0*x0 - 0.5*x0*x0 + 0.25*x0**4


def core_energy() -> float:
    # Minimum of V at psi=0 occurs at X^2=1 in the dimensionless model.
    return -0.25


def delta_v(a: float, b: float, c: float) -> float:
    dv = core_energy() - vacuum_energy(a, b, c)
    if dv <= 0:
        raise ValueError("vortex-bag bulk phase is not more energetic than the exterior vacuum")
    return float(dv)


def asymptotic_energy_per_flux(q: float, a: float, b: float, c: float) -> float:
    return float(2.0*np.pi*np.sqrt(2.0*delta_v(a,b,c))/q)


def e1(q: float, a: float, b: float, c: float, radius: float, points: int) -> float:
    sol = solve_vortex(a,b,c,q,1,radius=radius,points=points,tol=1e-6)
    return vortex_energy(sol,a,b,c,q,1,radius=radius,integration_points=10000)


def find_qinf(a=-0.8,b=1.0,c=0.4,qlo=1.2815,qhi=1.2830,radius=26.0,points=700):
    def f(q):
        return asymptotic_energy_per_flux(q,a,b,c) - e1(q,a,b,c,radius,points)
    return brentq(f,qlo,qhi,xtol=1e-10)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--a",type=float,default=-0.8)
    p.add_argument("--b",type=float,default=1.0)
    p.add_argument("--c",type=float,default=0.4)
    p.add_argument("--qlo",type=float,default=1.2815)
    p.add_argument("--qhi",type=float,default=1.2830)
    p.add_argument("--radius",type=float,default=26.0)
    p.add_argument("--points",type=int,default=700)
    args=p.parse_args()
    dv=delta_v(args.a,args.b,args.c)
    qinf=find_qinf(args.a,args.b,args.c,args.qlo,args.qhi,args.radius,args.points)
    print(f"DeltaV={dv:.12g}")
    print(f"q_c_infinity={qinf:.12g}")
    print(f"Einf_per_flux={asymptotic_energy_per_flux(qinf,args.a,args.b,args.c):.12g}")
    print(f"E1={e1(qinf,args.a,args.b,args.c,args.radius,args.points):.12g}")

if __name__ == "__main__":
    main()
