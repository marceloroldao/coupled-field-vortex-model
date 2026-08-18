"""V0.2 cross-parameter consistency test for the critical split.

For nearby neutral-scalar couplings c, independently compare

    delta_root = q_sigma - q_inf

with the planar linearization

    delta_lin = -sigma(q_inf) / sigma'(q_sigma).

No finite-n giant-vortex data are fitted.  The test asks whether the same
local identity explains the split at more than one admissible parameter point.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

from .v02_cross_parameter_split import (
    A, B, C_VALUES, find_qinf_general, find_qsigma_near, sigma_value
)


def sigma_derivative_4(q, a, b, c, h=2.5e-4):
    """Fourth-order central derivative using independently converged sigma values."""
    sm2=sigma_value(q-2*h,a,b,c)[1]
    sm1=sigma_value(q-h,a,b,c)[1]
    sp1=sigma_value(q+h,a,b,c)[1]
    sp2=sigma_value(q+2*h,a,b,c)[1]
    return (sm2-8*sm1+8*sp1-sp2)/(12*h)


def run(outdir="results/v02_validation"):
    out=Path(outdir); out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for c in C_VALUES:
        row={"a":A,"b":B,"c":c}
        try:
            qinf=find_qinf_general(A,B,c)
            qsigma,_=find_qsigma_near(qinf,A,B,c)
            sigma_inf=sigma_value(qinf,A,B,c)[1]
            dsigma=sigma_derivative_4(qsigma,A,B,c)
            delta_root=float(qsigma-qinf)
            delta_lin=float(-sigma_inf/dsigma)
            ratio=float(delta_lin/delta_root) if delta_root != 0 else float("nan")
            rel_mismatch=abs(delta_lin-delta_root)/max(abs(delta_root),1e-30)
            row.update({
                "converged":True,
                "q_inf":qinf,
                "q_sigma":qsigma,
                "delta_root":delta_root,
                "sigma_at_q_inf":sigma_inf,
                "dsigma_dq_at_q_sigma":dsigma,
                "delta_linearized":delta_lin,
                "ratio_linearized_to_root":ratio,
                "relative_mismatch":rel_mismatch,
                "consistent_within_10pct":bool(rel_mismatch <= 0.10),
                "message":""
            })
        except Exception as exc:
            row.update({"converged":False,"message":str(exc)})
        rows.append(row)

    fields=sorted({k for r in rows for k in r})
    with (out/"cross_parameter_linearization.csv").open("w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows(rows)

    good=[r for r in rows if r.get("converged")]
    consistent=[r for r in good if r.get("consistent_within_10pct")]
    nonzero=[r for r in good if abs(float(r["delta_root"]))>5e-6]
    same_sign=(len(nonzero)>=2 and (all(float(r["delta_root"])>0 for r in nonzero) or
                                   all(float(r["delta_root"])<0 for r in nonzero)))
    summary={
        "parameter_points":len(rows),
        "converged_points":len(good),
        "linearization_consistent_points":len(consistent),
        "nonzero_split_points":len(nonzero),
        "same_split_sign":same_sign,
        "status":"CROSS_PARAMETER_LINEARIZATION_SUPPORT" if (
            len(good)>=2 and len(consistent)==len(good) and len(nonzero)>=2 and same_sign
        ) else "INCOMPLETE",
        "note":"Support is numerical and local; novelty still requires literature audit and independent review."
    }
    (out/"cross_parameter_linearization_summary.json").write_text(
        json.dumps(summary,indent=2),encoding="utf-8"
    )
    print(json.dumps(summary,indent=2))
    for r in rows: print(r)
    return rows,summary


if __name__=="__main__":
    run()
