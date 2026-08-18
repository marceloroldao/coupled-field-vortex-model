"""V0.2 independent consistency test for the critical-point splitting.

Tests the first-order identity

    q_sigma - q_inf = -sigma(q_inf) / sigma'(q_sigma) + O((q_sigma-q_inf)^2)

using only planar-interface calculations plus the frozen q_inf reference.
Finite-n giant-vortex data are not used.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from .v02_critical_splitting import find_q_sigma, sigma_robust
from .v02_curvature_diagnostics import QREF


def sigma_value(q, *, L, points, tol=5e-7, max_nodes=350000):
    return float(sigma_robust(q,L=L,points=points,tol=tol,max_nodes=max_nodes)[1])


def derivative_symmetric(q, h, *, L, points):
    sm2=sigma_value(q-2*h,L=L,points=points)
    sm1=sigma_value(q-h,L=L,points=points)
    sp1=sigma_value(q+h,L=L,points=points)
    sp2=sigma_value(q+2*h,L=L,points=points)
    # Fourth-order central derivative.
    d=(-sp2 + 8*sp1 - 8*sm1 + sm2)/(12*h)
    return float(d), {"sigma_m2":sm2,"sigma_m1":sm1,"sigma_p1":sp1,"sigma_p2":sp2}


def run(outdir="results/v02_validation"):
    out=Path(outdir); out.mkdir(parents=True,exist_ok=True)
    configs=[(18.0,1900),(20.0,2300),(22.0,2700),(24.0,3100)]
    hs=(2e-4,1e-4,5e-5)
    rows=[]

    for L,points in configs:
        try:
            # Determine q_sigma with a domain-matched root rather than reusing a root
            # found at a different L.
            def f(q):
                return sigma_value(q,L=L,points=points)

            from scipy.optimize import brentq
            q_sigma=float(brentq(f,1.2820,1.2835,xtol=2e-11,rtol=2e-11,maxiter=60))
            sigma_inf=f(QREF)
            root_split=q_sigma-QREF

            for h in hs:
                deriv,stencil=derivative_symmetric(q_sigma,h,L=L,points=points)
                lin_split=-sigma_inf/deriv
                ratio=lin_split/root_split if root_split != 0 else np.nan
                rows.append({
                    "L":L,"points":points,"h":h,"q_sigma":q_sigma,"q_inf":QREF,
                    "sigma_q_inf":sigma_inf,"sigma_prime_q_sigma":deriv,
                    "delta_q_root":root_split,"delta_q_linearized":lin_split,
                    "split_ratio":ratio,"abs_ratio_minus_1":abs(ratio-1.0),
                    **stencil,
                    "converged":True,"message":""
                })
        except Exception as exc:
            rows.append({"L":L,"points":points,"h":"","q_sigma":"","q_inf":QREF,
                         "sigma_q_inf":"","sigma_prime_q_sigma":"","delta_q_root":"",
                         "delta_q_linearized":"","split_ratio":"","abs_ratio_minus_1":"",
                         "sigma_m2":"","sigma_m1":"","sigma_p1":"","sigma_p2":"",
                         "converged":False,"message":str(exc)})

    import csv
    path=out/"critical_split_linearization.csv"
    with path.open("w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    good=[r for r in rows if r["converged"]]
    if good:
        best_h=min(hs)
        tail=[r for r in good if float(r["h"])==best_h]
        max_ratio_err=max(float(r["abs_ratio_minus_1"]) for r in tail)
        spread=max(float(r["delta_q_root"]) for r in tail)-min(float(r["delta_q_root"]) for r in tail)
        split_min=min(abs(float(r["delta_q_root"])) for r in tail)
        classification=("CONSISTENT_SPLIT" if max_ratio_err < 0.10 and spread < 5e-6 and split_min > 5e-6
                        else "UNRESOLVED")
        summary={"classification":classification,"best_h":best_h,
                 "max_abs_ratio_minus_1":max_ratio_err,
                 "q_sigma_domain_spread":spread,"minimum_abs_split":split_min,
                 "note":"Frozen diagnostic; no finite-n giant-vortex data used."}
    else:
        summary={"classification":"INCOMPLETE","note":"No converged domain rows."}

    (out/"critical_split_linearization_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print(json.dumps(summary,indent=2))
    for r in rows: print(r)
    return rows,summary


if __name__=="__main__":
    run()
