"""V0.2 cross-parameter diagnostic for q_sigma versus q_inf.

Purpose
-------
Test whether the separation between the planar zero-tension point q_sigma and
the large-n bag critical root q_inf is a local accident of the reference
parameter c=0.4 or persists in a nearby admissible multifield regime.

This is exploratory validation, not a publication PASS gate.  Each parameter
point is solved independently; no finite-n giant-vortex data are fitted.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

from .large_n_bag_limit import asymptotic_energy_per_flux, e1, delta_v
from .planar_interface_tension import solve_interface
from .v02_curvature_diagnostics import curvature_observables

A=-0.8
B=1.0
C_VALUES=(0.35,0.40,0.45)


def bag_function(q,a,b,c,radius=26.0,points=700):
    return asymptotic_energy_per_flux(q,a,b,c)-e1(q,a,b,c,radius,points)


def adaptive_bracket(func, center=1.282, halfwidth=0.02, expansions=5, samples=17):
    for k in range(expansions):
        w=halfwidth*(2**k)
        xs=np.linspace(max(0.2,center-w),center+w,samples)
        vals=[]
        for x in xs:
            try:
                vals.append((float(x),float(func(float(x)))))
            except Exception:
                vals.append((float(x),None))
        for (x0,y0),(x1,y1) in zip(vals[:-1],vals[1:]):
            if y0 is None or y1 is None:
                continue
            if y0==0:
                return x0,x0
            if y0*y1<0:
                return x0,x1
    raise RuntimeError("failed to bracket root")


def find_qinf_general(a,b,c):
    f=lambda q: bag_function(q,a,b,c)
    lo,hi=adaptive_bracket(f)
    if lo==hi:
        return lo
    return float(brentq(f,lo,hi,xtol=2e-10,rtol=2e-10,maxiter=80))


def sigma_value(q,a,b,c,L=18.0,points=1800,tol=8e-7,max_nodes=250000):
    trials=[]
    for dq in (-2e-3,-1e-3,-5e-4,5e-4,1e-3):
        try:
            seed,_,_=solve_interface(q+dq,a=a,b=b,c=c,L=L,points=points,
                                     tol=max(5*tol,3e-6),max_nodes=max_nodes)
            sol,Hc,Vmix=solve_interface(q,a=a,b=b,c=c,L=L,points=points,
                                        tol=tol,guess=seed,max_nodes=max_nodes)
            obs=curvature_observables(sol,q,Hc,Vmix,a=a,b=b,c=c,L=L,
                                      integration_points=28000)
            trials.append((float(obs["solver_residual_max"]),float(obs["sigma"])))
        except Exception:
            continue
    if not trials:
        raise RuntimeError(f"no converged interface solution at q={q}")
    trials.sort(key=lambda t:t[0])
    return trials[0]


def find_qsigma_near(qinf,a,b,c):
    cache={}
    def f(q):
        q=float(q)
        if q not in cache:
            cache[q]=sigma_value(q,a,b,c)
        return cache[q][1]
    lo,hi=adaptive_bracket(f,center=qinf,halfwidth=0.01,expansions=4,samples=15)
    if lo==hi:
        return lo,cache
    return float(brentq(f,lo,hi,xtol=3e-10,rtol=3e-10,maxiter=80)),cache


def run(outdir="results/v02_validation"):
    out=Path(outdir); out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for c in C_VALUES:
        row={"a":A,"b":B,"c":c}
        try:
            dv=delta_v(A,B,c)
            qinf=find_qinf_general(A,B,c)
            qsigma,cache=find_qsigma_near(qinf,A,B,c)
            resid_inf,sigma_inf=sigma_value(qinf,A,B,c)
            resid_sig,sigma_sig=sigma_value(qsigma,A,B,c)
            delta=float(qsigma-qinf)
            row.update({
                "converged":True,
                "DeltaV":dv,
                "q_inf":qinf,
                "q_sigma":qsigma,
                "delta_q":delta,
                "sigma_at_q_inf":sigma_inf,
                "sigma_at_q_sigma":sigma_sig,
                "residual_q_inf":resid_inf,
                "residual_q_sigma":resid_sig,
                "classification":"SPLIT" if abs(delta)>5e-6 else "UNRESOLVED_OR_COINCIDENT",
                "message":""
            })
        except Exception as exc:
            row.update({"converged":False,"message":str(exc)})
        rows.append(row)

    fields=sorted({k for r in rows for k in r})
    with (out/"cross_parameter_split.csv").open("w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows(rows)

    good=[r for r in rows if r.get("converged")]
    same_sign=False
    if len(good)>=2:
        ds=[float(r["delta_q"]) for r in good if abs(float(r["delta_q"]))>5e-6]
        same_sign=(len(ds)>=2 and (all(d>0 for d in ds) or all(d<0 for d in ds)))
    summary={
        "parameter_points":len(rows),
        "converged_points":len(good),
        "stable_nonzero_sign_across_points":same_sign,
        "status":"CROSS_PARAMETER_SUPPORT" if len(good)>=2 and same_sign else "INCOMPLETE",
        "note":"Exploratory nearby-c scan; not a novelty or publication gate by itself."
    }
    (out/"cross_parameter_split_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print(json.dumps(summary,indent=2))
    for r in rows: print(r)
    return rows,summary


if __name__=="__main__":
    run()
