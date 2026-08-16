"""V0.2 exploratory residual-scaling diagnostic.

This diagnostic does not fit or modify the independently derived two-term
coefficients. It asks what power law remains after subtracting

    alpha_sigma n^(-1/2) + alpha_1 n^(-1).

The output is descriptive only. No PASS threshold is introduced here because
the high-winding data were already inspected during development.
"""
from __future__ import annotations

import csv
from pathlib import Path
import numpy as np

from .v02_two_term_prediction import run as run_two_term


def run(outdir="results/v02_validation"):
    out=Path(outdir); out.mkdir(parents=True, exist_ok=True)
    _,rows=run_two_term(outdir=outdir)
    high=[r for r in rows if r["group"]=="high"]
    n=np.array([float(r["n"]) for r in high],dtype=float)
    residual=np.array([float(r["residual"]) for r in high],dtype=float)

    mask=np.isfinite(residual) & (residual!=0)
    slope=float(np.polyfit(np.log(n[mask]),np.log(np.abs(residual[mask])),1)[0])

    records=[]
    for i,(ni,ri) in enumerate(zip(n,residual)):
        local_slope=""
        if i>0 and residual[i-1]!=0 and ri!=0:
            local_slope=float(
                np.log(abs(ri/residual[i-1]))/np.log(ni/n[i-1])
            )
        records.append({
            "n":int(ni),
            "residual":float(ri),
            "residual_times_sqrt_n":float(ri*np.sqrt(ni)),
            "residual_times_n":float(ri*ni),
            "residual_times_n_3_over_2":float(ri*ni**1.5),
            "local_effective_slope":local_slope,
        })

    with (out/"two_term_residual_scaling.csv").open("w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=list(records[0].keys()))
        w.writeheader(); w.writerows(records)

    (out/"two_term_residual_scaling_summary.txt").write_text(
        f"global_loglog_slope={slope:.16g}\n"
        "reference_slope_for_n^-3/2=-1.5\n"
        "status=EXPLORATORY\n",
        encoding="utf-8",
    )

    print(f"global_loglog_slope={slope:.12g}")
    print("reference_slope_for_n^-3/2=-1.5")
    for r in records:
        print(r)
    return slope,records


if __name__=="__main__":
    run()
