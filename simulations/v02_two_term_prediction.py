"""V0.2 exploratory two-term prediction.

Uses independently computed planar sigma and candidate A0 to predict

    q_c^(n)-q_inf = alpha_sigma n^(-1/2) + alpha_1 n^(-1)

without calibrating either coefficient on giant-vortex q_c^(n) data.

A0 is still exploratory because the boundary/ensemble closure and strict
convergence gate are not complete. Therefore this module reports diagnostics
but does not promote G3/G4 to PASS.
"""
from __future__ import annotations

import csv
from pathlib import Path
import numpy as np

from .v02_sigma_leading_prediction import derive_prediction, N_VALID, QC_VALID, QINF
from .v02_curvature_diagnostics import solve_with_seed, curvature_observables

A=-0.8
B=1.0
C=0.4

# High-winding values are validation-only. They are not used to calculate
# alpha_sigma or alpha_1.
N_HIGH=np.array([16,20,24,32,64,128], dtype=float)
QC_HIGH=np.array([
    1.2823450021208787,
    1.2822856180749810,
    1.2822490744391220,
    1.2822078277947904,
    1.2821584946080210,
    1.2821446722518808,
], dtype=float)


def independent_a0(q=QINF, L=16.0, points=1200, tol=2e-6):
    sol,Hc,Vmix=solve_with_seed(q,a=A,b=B,c=C,L=L,points=points,tol=tol)
    obs=curvature_observables(sol,q,Hc,Vmix,a=A,b=B,c=C,L=L,
                              integration_points=22000)
    return obs


def run(outdir="results/v02_validation"):
    out=Path(outdir); out.mkdir(parents=True, exist_ok=True)
    base=derive_prediction()
    obs=independent_a0()
    a0=float(obs["A0_candidate"])
    alpha1=float(-2.0*np.pi*a0/base["Fprime"])
    alpha_sigma=float(base["alpha_sigma"])
    n_cross=float((alpha1/alpha_sigma)**2) if alpha_sigma*alpha1 < 0 else np.nan

    derived={
        **base,
        "A0_candidate":a0,
        "alpha_1_candidate":alpha1,
        "n_cross_candidate":n_cross,
        "A0_solver_residual":float(obs["solver_residual_max"]),
        "A0_nodes":int(obs["final_node_count"]),
    }

    rows=[]
    for group,N,QC in (("moderate",N_VALID,QC_VALID),("high",N_HIGH,QC_HIGH)):
        for n,qobs in zip(N,QC):
            p_sigma=alpha_sigma/np.sqrt(n)
            p_a1=alpha1/n
            shift=p_sigma+p_a1
            qpred=QINF+shift
            rows.append({
                "group":group,"n":int(n),"q_observed":float(qobs),
                "q_pred_two_term":float(qpred),
                "observed_shift":float(qobs-QINF),
                "sigma_term":float(p_sigma),"A0_term":float(p_a1),
                "predicted_shift":float(shift),
                "residual":float(qobs-qpred),
            })

    with (out/"two_term_prediction.csv").open("w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    (out/"two_term_summary.txt").write_text(
        "\n".join(f"{k}={v}" for k,v in derived.items())+"\n",encoding="utf-8")

    print("Independent exploratory coefficients:")
    for k,v in derived.items(): print(f"{k}={v}")
    print("Validation-only comparison:")
    for r in rows: print(r)
    return derived,rows


if __name__ == "__main__":
    run()
