"""V0.2 diagnostic: compare the planar zero-tension point with the large-n bag root.

This script uses only the planar interface solver plus the independently frozen
large-n reference q_inf from V0.1. It does not fit giant-vortex finite-n data.

Scientific purpose
------------------
The V0.2 curvature program revealed that sigma(q_inf) is small but nonzero.
That means two a priori different critical notions may be split:

1. q_sigma: planar normal/mixed interface has sigma=0;
2. q_inf: large-n radial/bag critical root.

If q_sigma != q_inf reproducibly, curvature coefficients evaluated at q_inf
must retain an explicit dividing-surface/radius convention because sigma != 0.
At q_sigma the first-moment translation ambiguity proportional to sigma
vanishes, providing a cleaner diagnostic point for interface curvature.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

from .planar_interface_tension import solve_interface
from .v02_curvature_diagnostics import curvature_observables, QREF

A=-0.8
B=1.0
C=0.4


def sigma_robust(q, *, L=18.0, points=1800, tol=5e-7, max_nodes=250000):
    """Evaluate sigma with several continuation seeds and keep best residual."""
    trials=[]
    for dq in (-2e-3,-1e-3,-5e-4,5e-4,1e-3):
        try:
            seed,_,_=solve_interface(q+dq,a=A,b=B,c=C,L=L,points=points,
                                     tol=max(5*tol,2e-6),max_nodes=max_nodes)
            sol,Hc,Vmix=solve_interface(q,a=A,b=B,c=C,L=L,points=points,
                                        tol=tol,guess=seed,max_nodes=max_nodes)
            obs=curvature_observables(sol,q,Hc,Vmix,a=A,b=B,c=C,L=L,
                                      integration_points=32000)
            trials.append((obs["solver_residual_max"],obs["sigma"],sol,Hc,Vmix,obs,dq))
        except Exception:
            continue
    if not trials:
        raise RuntimeError(f"no converged interface solution at q={q}")
    trials.sort(key=lambda t:t[0])
    return trials[0]


def find_q_sigma(qlo=1.2820,qhi=1.2835):
    cache={}
    def f(q):
        key=float(q)
        if key not in cache:
            cache[key]=sigma_robust(key)
        return float(cache[key][1])
    flo=f(qlo); fhi=f(qhi)
    if flo*fhi>0:
        raise RuntimeError(f"sigma root not bracketed: sigma({qlo})={flo}, sigma({qhi})={fhi}")
    root=brentq(f,qlo,qhi,xtol=2e-11,rtol=2e-11,maxiter=60)
    best=sigma_robust(root)
    return root,best,cache


def run(outdir="results/v02_validation"):
    out=Path(outdir); out.mkdir(parents=True,exist_ok=True)
    q_sigma,best,cache=find_q_sigma()
    resid,sigma,sol,Hc,Vmix,obs,dq=best

    # Independently evaluate q_inf with same numerical setup for a clean comparison.
    inf_best=sigma_robust(QREF)
    inf_resid,inf_sigma,_,_,_,inf_obs,inf_dq=inf_best

    delta=float(q_sigma-QREF)
    summary={
        "q_sigma":float(q_sigma),
        "q_inf":float(QREF),
        "delta_q_sigma_minus_q_inf":delta,
        "sigma_at_q_sigma":float(sigma),
        "sigma_at_q_inf":float(inf_sigma),
        "solver_residual_q_sigma":float(resid),
        "solver_residual_q_inf":float(inf_resid),
        "A0_candidate_q_sigma":float(obs["A0_candidate"]),
        "A0_candidate_q_inf":float(inf_obs["A0_candidate"]),
        "shift_identity_error_q_sigma":float(obs["shift_identity_error"]),
        "shift_identity_error_q_inf":float(inf_obs["shift_identity_error"]),
        "classification":"SPLIT" if abs(delta)>5e-6 else "UNRESOLVED_OR_COINCIDENT",
        "note":"Diagnostic only; novelty requires literature audit and cross-parameter validation."
    }
    (out/"critical_splitting.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    rows=[]
    for q,t in sorted(cache.items()):
        rows.append({"q":q,"sigma":t[1],"solver_residual_max":t[0],"seed_offset":t[6]})
    with (out/"critical_splitting_scan.csv").open("w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=["q","sigma","solver_residual_max","seed_offset"])
        w.writeheader(); w.writerows(rows)

    print(json.dumps(summary,indent=2))
    return summary


if __name__=="__main__":
    run()
