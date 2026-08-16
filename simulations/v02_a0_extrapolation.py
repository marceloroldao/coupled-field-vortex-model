"""V0.2 robust A0 domain-convergence and extrapolation diagnostic.

This script does not use giant-vortex data. It attacks only the numerical
closure of the planar curvature coefficient candidate A0 by:

1. solving the same planar interface at several domain sizes L;
2. trying several q-continuation seed offsets when a BVP branch is delicate;
3. choosing the converged solution with the smallest reported BVP residual;
4. comparing simple finite-domain extrapolation families using only A0(L);
5. repeating the extrapolation on the asymptotic tail to diagnose whether
   small-L points bias the inferred infinite-domain limit.

The extrapolation is diagnostic, not yet a scientific PASS gate. In
particular, a finite A0(infinity) estimate is not promoted to a physical
curvature coefficient until the boundary/ensemble and radius-convention
closure is complete.
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy.optimize import curve_fit

from .planar_interface_tension import solve_interface
from .v02_curvature_diagnostics import QREF, curvature_observables

A=-0.8
B=1.0
C=0.4


def solve_best(q, *, L, points, tol, max_nodes, seed_offsets):
    trials=[]
    for dq in seed_offsets:
        try:
            seed,_,_=solve_interface(q+dq,a=A,b=B,c=C,L=L,points=points,
                                     tol=max(5*tol,2e-6),max_nodes=max_nodes)
            sol,Hc,Vmix=solve_interface(q,a=A,b=B,c=C,L=L,points=points,
                                        tol=tol,guess=seed,max_nodes=max_nodes)
            resid=float(np.max(sol.rms_residuals))
            trials.append((resid,dq,sol,Hc,Vmix))
        except Exception:
            continue
    if not trials:
        raise RuntimeError("all continuation seeds failed")
    trials.sort(key=lambda t:t[0])
    return trials[0]


def _fit_linear_basis(L,y,power):
    X=np.column_stack([np.ones_like(L),L**(-power)])
    beta=np.linalg.lstsq(X,y,rcond=None)[0]
    pred=X@beta
    rss=float(np.sum((y-pred)**2))
    return float(beta[0]),float(beta[1]),rss,pred


def _fit_exp(L,y):
    def f(x,ainf,c,mu):
        return ainf+c*np.exp(-mu*x)
    p0=[float(y[-1]),float(y[0]-y[-1]),0.25]
    popt,_=curve_fit(f,L,y,p0=p0,maxfev=50000,
                     bounds=([-np.inf,-np.inf,1e-5],[np.inf,np.inf,5.0]))
    pred=f(L,*popt)
    rss=float(np.sum((y-pred)**2))
    return tuple(float(v) for v in popt),rss,pred


def _aicc(rss,n,k):
    rss=max(rss,1e-300)
    aic=n*np.log(rss/n)+2*k
    if n<=k+1:
        return float("inf")
    return float(aic + 2*k*(k+1)/(n-k-1))


def _summarize_models(L,y,label):
    summary=[]
    for power,name in ((1.0,"Ainf+c/L"),(2.0,"Ainf+c/L^2")):
        ainf,c,rss,_=_fit_linear_basis(L,y,power)
        summary.append({"fit_set":label,"model":name,"A0_infinity":ainf,
                        "aux1":c,"aux2":"","rss":rss,
                        "aicc":_aicc(rss,len(L),2),"n_points":len(L),
                        "L_min":float(np.min(L)),"L_max":float(np.max(L))})
    try:
        (ainf,c,mu),rss,_=_fit_exp(L,y)
        summary.append({"fit_set":label,"model":"Ainf+c*exp(-mu L)",
                        "A0_infinity":ainf,"aux1":c,"aux2":mu,"rss":rss,
                        "aicc":_aicc(rss,len(L),3),"n_points":len(L),
                        "L_min":float(np.min(L)),"L_max":float(np.max(L))})
    except Exception as exc:
        summary.append({"fit_set":label,"model":"Ainf+c*exp(-mu L)",
                        "A0_infinity":"","aux1":"","aux2":"","rss":"",
                        "aicc":"","n_points":len(L),"L_min":float(np.min(L)),
                        "L_max":float(np.max(L)),"error":str(exc)})
    return summary


def run(outdir="results/v02_validation"):
    out=Path(outdir); out.mkdir(parents=True,exist_ok=True)
    tol=5e-7
    max_nodes=400000
    configs=[
        (14.,1100),(16.,1500),(18.,1900),(20.,2300),(22.,2700),(24.,3100),
        (26.,3500),(28.,3900),(30.,4300),
    ]
    seed_offsets=(-2e-3,-1e-3,-5e-4,5e-4)
    rows=[]
    for L,points in configs:
        try:
            resid,dq,sol,Hc,Vmix=solve_best(QREF,L=L,points=points,tol=tol,
                                             max_nodes=max_nodes,
                                             seed_offsets=seed_offsets)
            obs=curvature_observables(sol,QREF,Hc,Vmix,a=A,b=B,c=C,L=L,
                                      integration_points=36000)
            rows.append({"L":L,"points":points,"converged":True,
                         "seed_offset":dq,"solver_residual_max":resid,
                         "sigma":obs["sigma"],"A0_candidate":obs["A0_candidate"],
                         "M1":obs["M1"],"Kgeom":obs["Kgeom"],"message":""})
        except Exception as exc:
            rows.append({"L":L,"points":points,"converged":False,
                         "seed_offset":"","solver_residual_max":"","sigma":"",
                         "A0_candidate":"","M1":"","Kgeom":"","message":str(exc)})

    with (out/"a0_domain_scan.csv").open("w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    good=[r for r in rows if r["converged"]]
    summary=[]
    if len(good)>=4:
        L=np.array([float(r["L"]) for r in good])
        y=np.array([float(r["A0_candidate"]) for r in good])
        summary.extend(_summarize_models(L,y,"all_converged"))

        tail_mask=L>=18.0
        if int(np.sum(tail_mask))>=4:
            summary.extend(_summarize_models(L[tail_mask],y[tail_mask],"tail_L_ge_18"))

        deep_mask=L>=22.0
        if int(np.sum(deep_mask))>=4:
            summary.extend(_summarize_models(L[deep_mask],y[deep_mask],"tail_L_ge_22"))

    if summary:
        fields=sorted({k for r in summary for k in r})
        with (out/"a0_extrapolation_models.csv").open("w",newline="",encoding="utf-8") as fh:
            w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows(summary)

    print("A0 domain scan:")
    for r in rows: print(r)
    print("Extrapolation diagnostics (planar data only):")
    for r in summary: print(r)
    return rows,summary


if __name__=="__main__":
    run()
