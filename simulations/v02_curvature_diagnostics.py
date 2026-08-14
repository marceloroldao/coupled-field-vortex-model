"""V0.2 G2 exploratory curvature diagnostics.

This module evaluates the first explicit curvature functional derived from the
planar Gibbs interface without fitting to giant-vortex data.

The current quantity

    A0 = int [z*g0 + A*(B-Hc)] dz

is a candidate constant-in-R wall coefficient in the fixed planar gauge/origin
convention.  It is NOT yet promoted to the final invariant giant-vortex
curvature coefficient; boundary/ensemble and radius-convention closure remains
part of G2.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
from scipy.integrate import simpson

from .planar_interface_tension import solve_interface, potential


QREF = 1.2821745509961426


def observables(sol, Hc, Vmix, a=-0.8, b=1.0, c=0.4, L=14.0,
                integration_points=16000, origin_shift=1.0):
    z = np.linspace(-L, L, integration_points)
    f, fp, x, xp, A, B = sol.sol(z)
    g0 = (
        fp**2
        + (A*A*f*f) * 0.0  # replaced below using q supplied through sol wrapper
    )
    raise RuntimeError("observables requires q; use curvature_observables")


def curvature_observables(sol, q, Hc, Vmix, a=-0.8, b=1.0, c=0.4,
                          L=14.0, integration_points=16000,
                          origin_shift=1.0):
    z = np.linspace(-L, L, integration_points)
    f, fp, x, xp, A, B = sol.sol(z)
    g0 = (
        fp**2
        + q*q*A*A*f*f
        + 0.5*xp**2
        + 0.5*B**2
        + potential(f, x, a, b, c)
        - Hc*B
        - Vmix
    )
    sigma = float(simpson(g0, x=z))
    m1 = float(simpson(z*g0, x=z))
    kgeom = float(simpson(A*(B-Hc), x=z))
    a0 = m1 + kgeom

    d = float(origin_shift)
    m1_shift = float(simpson((z-d)*g0, x=z))
    shift_identity_error = (m1_shift - m1) + d*sigma
    a0_shift = m1_shift + kgeom

    residual = float(np.max(sol.rms_residuals)) if getattr(sol, "rms_residuals", None) is not None else np.nan
    return {
        "sigma": sigma,
        "M1": m1,
        "Kgeom": kgeom,
        "A0_candidate": a0,
        "M1_shift": m1_shift,
        "A0_shift": a0_shift,
        "shift_identity_error": float(shift_identity_error),
        "solver_residual_max": residual,
        "final_node_count": int(sol.x.size),
    }


def solve_with_seed(q, *, a, b, c, L, points, tol):
    # Seed slightly below q because the exact near-zero-tension point can be
    # numerically delicate for a cold start. Continuation changes only the
    # initial guess, not equations or tolerances.
    seed_q = q - 1.0e-3
    seed, _, _ = solve_interface(seed_q, a=a, b=b, c=c, L=L,
                                 points=points, tol=tol)
    return solve_interface(q, a=a, b=b, c=c, L=L,
                           points=points, tol=tol, guess=seed)


def run(mode="quick", outdir="results/v02_validation", a=-0.8, b=1.0, c=0.4,
        qref=QREF):
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    tol = 2e-5 if mode == "quick" else 5e-7
    configs = (
        [(12.0, 500), (14.0, 700), (16.0, 900)]
        if mode == "quick"
        else [(12.0, 800), (14.0, 1100), (16.0, 1500), (18.0, 1900)]
    )
    rows = []
    for L, points in configs:
        try:
            sol, Hc, Vmix = solve_with_seed(
                qref, a=a, b=b, c=c, L=L, points=points, tol=tol
            )
            obs = curvature_observables(
                sol, qref, Hc, Vmix, a=a, b=b, c=c, L=L,
                integration_points=12000 if mode == "quick" else 26000,
            )
            row = {
                "mode": mode, "q": qref, "L": L, "points": points,
                "tol": tol, "converged": True, "message": "", **obs,
            }
        except Exception as exc:
            row = {
                "mode": mode, "q": qref, "L": L, "points": points,
                "tol": tol, "converged": False, "message": str(exc),
                "sigma": "", "M1": "", "Kgeom": "",
                "A0_candidate": "", "M1_shift": "", "A0_shift": "",
                "shift_identity_error": "", "solver_residual_max": "",
                "final_node_count": "",
            }
        rows.append(row)

    path = out / "curvature_convergence.csv"
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    # Exploratory status only. We intentionally do not freeze a scientific
    # PASS threshold for A0 before boundary/ensemble closure is complete.
    converged = [r for r in rows if r["converged"]]
    print(f"mode={mode} qref={qref:.12g} converged={len(converged)}/{len(rows)}")
    for r in rows:
        print(r)
    return rows


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["quick", "full"], default="quick")
    p.add_argument("--qref", type=float, default=QREF)
    p.add_argument("--outdir", default="results/v02_validation")
    args = p.parse_args()
    run(args.mode, args.outdir, qref=args.qref)


if __name__ == "__main__":
    main()
