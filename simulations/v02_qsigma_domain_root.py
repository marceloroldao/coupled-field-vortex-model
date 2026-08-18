"""V0.2 diagnostic: test domain convergence of the planar zero-tension root q_sigma.

This script determines q_sigma independently at several domain sizes L using
only the planar interface condition sigma(q)=0.  Its purpose is to decide
whether the apparent splitting q_sigma - q_inf is numerically stable before it
is interpreted physically.

No finite-n giant-vortex data are used.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

from scipy.optimize import brentq

from .v02_critical_splitting import sigma_robust
from .v02_curvature_diagnostics import QREF


def root_for_domain(L, points, qlo=1.2820, qhi=1.2835, tol=5e-7, max_nodes=350000):
    cache={}
    def f(q):
        q=float(q)
        if q not in cache:
            cache[q]=sigma_robust(q,L=L,points=points,tol=tol,max_nodes=max_nodes)
        return float(cache[q][1])
    flo=f(qlo); fhi=f(qhi)
    if flo*fhi>0:
        raise RuntimeError(f"root not bracketed at L={L}: {flo}, {fhi}")
    root=brentq(f,qlo,qhi,xtol=2e-11,rtol=2e-11,maxiter=60)
    best=sigma_robust(root,L=L,points=points,tol=tol,max_nodes=max_nodes)
    return root,best


def run(outdir="results/v02_validation"):
    out=Path(outdir); out.mkdir(parents=True,exist_ok=True)
    configs=[(16.0,1500),(18.0,1900),(20.0,2300),(22.0,2700),(24.0,3100)]
    rows=[]
    for L,points in configs:
        try:
            q_sigma,best=root_for_domain(L,points)
            resid,sigma,_,_,_,obs,seed=best
            rows.append({
                "L":L,"points":points,"converged":True,
                "q_sigma":q_sigma,"q_inf":QREF,
                "delta_q":q_sigma-QREF,"sigma_at_root":sigma,
                "solver_residual_max":resid,"seed_offset":seed,
                "A0_candidate":obs["A0_candidate"],"message":""
            })
        except Exception as exc:
            rows.append({
                "L":L,"points":points,"converged":False,
                "q_sigma":"","q_inf":QREF,"delta_q":"",
                "sigma_at_root":"","solver_residual_max":"","seed_offset":"",
                "A0_candidate":"","message":str(exc)
            })

    csv_path=out/"qsigma_domain_roots.csv"
    with csv_path.open("w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    good=[r for r in rows if r["converged"]]
    summary={"converged":len(good),"total":len(rows),"q_inf":QREF}
    if len(good)>=2:
        vals=[float(r["q_sigma"]) for r in good]
        deltas=[float(r["delta_q"]) for r in good]
        summary.update({
            "q_sigma_min":min(vals),"q_sigma_max":max(vals),
            "q_sigma_spread":max(vals)-min(vals),
            "delta_q_min":min(deltas),"delta_q_max":max(deltas),
            "tail_q_sigma_change":abs(vals[-1]-vals[-2]),
            "classification":"STABLE_SPLIT" if min(abs(d) for d in deltas)>5e-6 and (max(vals)-min(vals))<5e-6 else "UNRESOLVED"
        })
    (out/"qsigma_domain_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    print(json.dumps(summary,indent=2))
    for r in rows: print(r)
    return rows,summary


if __name__=="__main__":
    run()
