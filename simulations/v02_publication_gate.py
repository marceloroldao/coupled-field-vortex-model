"""Frozen V0.2 publication-readiness gate.

This script does not decide novelty. It checks whether the numerical/scientific
package is internally mature enough to justify a literature-priority audit and
paper drafting. It reads machine-readable V0.2 evidence already produced in
results/v02_validation/ and classifies the package conservatively.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

OUT=Path("results/v02_validation")


def load_json(name):
    p=OUT/name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def load_csv(name):
    p=OUT/name
    if not p.exists():
        return None
    with p.open(encoding="utf-8",newline="") as fh:
        return list(csv.DictReader(fh))


def as_bool(v):
    return str(v).lower() in {"true","1","yes"}


def main():
    checks={}

    # 1) Cross-parameter support for nonzero q_sigma-q_inf.
    cross=load_json("cross_parameter_split_summary.json")
    checks["cross_parameter_split"] = bool(cross and cross.get("status")=="CROSS_PARAMETER_SUPPORT")

    # 2) Reference-domain root stability.
    qdom=load_json("qsigma_domain_root_summary.json")
    checks["reference_split_domain_stability"] = bool(qdom and qdom.get("classification")=="STABLE_SPLIT")

    # 3) Independent linearization consistency at the reference point.
    lin=load_json("split_linearization_summary.json")
    checks["reference_linearization"] = bool(lin and lin.get("classification")=="CONSISTENT_SPLIT")

    # 4) Cross-parameter linearization consistency, if generated.
    xlin=load_json("cross_parameter_linearization_summary.json")
    checks["cross_parameter_linearization"] = bool(xlin and xlin.get("status")=="CROSS_PARAMETER_LINEARIZATION_SUPPORT")

    # 5) Require at least three converged q_sigma curvature-domain points.
    curv=load_csv("qsigma_curvature_convergence.csv")
    ncurv=sum(as_bool(r.get("converged")) for r in curv) if curv else 0
    checks["qsigma_curvature_numerical_support"] = ncurv >= 3

    # A package is numerically paper-ready only if all frozen core checks pass.
    core=[
        "cross_parameter_split",
        "reference_split_domain_stability",
        "reference_linearization",
        "cross_parameter_linearization",
        "qsigma_curvature_numerical_support",
    ]
    ready=all(checks[k] for k in core)
    summary={
        "gate":"V0.2 publication-readiness numerical gate",
        "checks":checks,
        "core_checks":core,
        "numerically_ready_for_literature_audit_and_paper_draft":ready,
        "classification":"NUMERICALLY_PAPER_READY" if ready else "INCOMPLETE",
        "important_note":(
            "Passing this gate is not a novelty claim. Publication still requires "
            "literature-priority audit, clear uncertainty accounting, and a final "
            "reproducibility run from a clean checkout."
        ),
    }
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"publication_gate.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print(json.dumps(summary,indent=2))
    return 0 if ready else 2


if __name__=="__main__":
    raise SystemExit(main())
