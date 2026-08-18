"""V0.2 zero-tension curvature convergence diagnostic.

This diagnostic first determines q_sigma from the planar interface condition
sigma(q_sigma)=0 and then evaluates the candidate constant curvature sector at
that same zero-tension point across several domain sizes.  Because the
translation shift of the first moment is proportional to sigma, q_sigma is the
cleanest point for testing whether the candidate A0 sector has a stable planar
limit before any mapping to giant-vortex data is attempted.

No finite-n giant-vortex data are used here.
"""
from __future__ import annotations

import csv
from pathlib import Path

from .v02_critical_splitting import find_q_sigma, sigma_robust
from .v02_curvature_diagnostics import curvature_observables


def run(outdir="results/v02_validation"):
    out=Path(outdir); out.mkdir(parents=True,exist_ok=True)
    q_sigma,_,_=find_q_sigma()
    configs=[(16.0,1500),(18.0,1900),(20.0,2300),(22.0,2700),(24.0,3100)]
    rows=[]
    for L,points in configs:
        try:
            resid,sigma,sol,Hc,Vmix,_,seed=sigma_robust(
                q_sigma,L=L,points=points,tol=5e-7,max_nodes=350000
            )
            obs=curvature_observables(
                sol,q_sigma,Hc,Vmix,L=L,integration_points=36000
            )
            rows.append({
                "q_sigma":q_sigma,"L":L,"points":points,"converged":True,
                "seed_offset":seed,"sigma":sigma,
                "A0_candidate":obs["A0_candidate"],"M1":obs["M1"],
                "Kgeom":obs["Kgeom"],"shift_identity_error":obs["shift_identity_error"],
                "solver_residual_max":resid,"message":""
            })
        except Exception as exc:
            rows.append({
                "q_sigma":q_sigma,"L":L,"points":points,"converged":False,
                "seed_offset":"","sigma":"","A0_candidate":"","M1":"",
                "Kgeom":"","shift_identity_error":"","solver_residual_max":"",
                "message":str(exc)
            })
    path=out/"qsigma_curvature_convergence.csv"
    with path.open("w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    good=[r for r in rows if r["converged"]]
    print(f"q_sigma={q_sigma:.12g} converged={len(good)}/{len(rows)}")
    for r in rows: print(r)
    if len(good)>=2:
        tail=good[-2:]
        a0a=float(tail[0]["A0_candidate"]); a0b=float(tail[1]["A0_candidate"])
        rel=abs(a0b-a0a)/max(abs(a0b),1e-30)
        print(f"tail_relative_A0_change={rel:.6e}")
    return rows


if __name__=="__main__":
    run()
