"""High-winding fusion-boundary scan for the coupled-field vortex model.

Locally reproduced companion to `radial_vortex_solver.py`.
For each winding n, solve Delta_n(q) = E_n(q) - n E_1(q) = 0.

Default model point:
    a=-0.8, b=1.0, c=0.4

This script is intended to reproduce the n=2,3,4,5,6,8,10,12 scan
reported under results/qc_high_winding_scan.md.
"""
from __future__ import annotations

import argparse
import numpy as np
from scipy.optimize import brentq

from radial_vortex_solver import solve_vortex, vortex_energy


def energy(q: float, n: int, a: float, b: float, c: float,
           radius: float, points: int, tol: float) -> float:
    sol = solve_vortex(a, b, c, q, n, radius=radius, points=points, tol=tol)
    return vortex_energy(sol, a, b, c, q, n, radius=radius)


def delta_n(q: float, n: int, a: float, b: float, c: float,
            radius: float, points: int, tol: float) -> float:
    e1 = energy(q, 1, a, b, c, radius, points, tol)
    en = energy(q, n, a, b, c, radius, points, tol)
    return en - n * e1


def critical_q(n: int, a: float, b: float, c: float,
               radius: float, points: int, tol: float,
               q_lo: float, q_hi: float) -> float:
    return float(brentq(
        lambda q: delta_n(q, n, a, b, c, radius, points, tol),
        q_lo, q_hi, xtol=2e-9
    ))


def extrapolate(ns: np.ndarray, qs: np.ndarray, order: int) -> tuple[float, np.ndarray]:
    cols = [np.ones_like(ns, dtype=float)]
    cols += [(1.0 / ns) ** k for k in range(1, order + 1)]
    X = np.vstack(cols).T
    coeff = np.linalg.lstsq(X, qs, rcond=None)[0]
    return float(coeff[0]), coeff


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, nargs="*", default=[2,3,4,5,6,8,10,12])
    p.add_argument("--a", type=float, default=-0.8)
    p.add_argument("--b", type=float, default=1.0)
    p.add_argument("--c", type=float, default=0.4)
    p.add_argument("--radius", type=float, default=22.0)
    p.add_argument("--points", type=int, default=500)
    p.add_argument("--tol", type=float, default=1e-5)
    p.add_argument("--q-lo", type=float, default=1.275)
    p.add_argument("--q-hi", type=float, default=1.295)
    args = p.parse_args()

    rows = []
    print("n,qc")
    for n in args.n:
        qc = critical_q(n, args.a, args.b, args.c,
                        args.radius, args.points, args.tol,
                        args.q_lo, args.q_hi)
        rows.append((n, qc))
        print(f"{n},{qc:.12f}")

    ns = np.array([r[0] for r in rows], dtype=float)
    qs = np.array([r[1] for r in rows], dtype=float)
    for order in (1, 2, 3):
        qinf, _ = extrapolate(ns, qs, order)
        print(f"qinf_order_{order},{qinf:.12f}")


if __name__ == "__main__":
    main()
