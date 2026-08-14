"""V0.2 G3: parameter-free leading finite-winding prediction.

Derives the n^(-1/2) correction to q_c^(n) from independently computed planar
interface tension sigma at q_c^(infinity), without fitting giant-vortex data.

For the large-n bag energy per flux quantum,

    E_n/n = E_inf(q) + beta_sigma(q) n^(-1/2) + ...

with

    beta_sigma = 2*pi*sigma*sqrt(C_R),
    C_R = sqrt(2)/(q*sqrt(DeltaV)),

because R_0 = sqrt(C_R*n).

At F(q)=E_inf(q)-E_1(q)=0, linearization gives

    q_c^(n)-q_inf = alpha_sigma n^(-1/2) + ...
    alpha_sigma = -beta_sigma/F'(q_inf).

The radial q_c^(n) values below are used only after alpha_sigma is fixed, as
validation data; they do not enter the coefficient calculation.
"""
from __future__ import annotations

import csv
from pathlib import Path
import numpy as np

from .large_n_bag_limit import delta_v, asymptotic_energy_per_flux, e1
from .planar_interface_tension import tension_with_solution

A = -0.8
B = 1.0
C = 0.4
QINF = 1.2821745509961426

# Existing independently reproduced radial fusion boundaries from the V0.1/V0.2
# numerical baseline. These are validation-only values.
N_VALID = np.array([2, 3, 4, 5, 6, 8, 10, 12], dtype=float)
QC_VALID = np.array([
    1.28591955,
    1.28434393,
    1.28362384,
    1.28322810,
    1.28298327,
    1.2827023687,
    1.2825490774,
    1.2824542123,
], dtype=float)


def interface_sigma(q: float, L=16.0, points=1000, tol=2e-6) -> float:
    seed_q = q - 1.0e-3
    _, seed = tension_with_solution(seed_q, a=A, b=B, c=C, L=L,
                                    points=points, tol=tol)
    sigma, _ = tension_with_solution(q, a=A, b=B, c=C, L=L,
                                     points=points, tol=tol, guess=seed)
    return float(sigma)


def F(q: float, radius=26.0, points=700) -> float:
    return (
        asymptotic_energy_per_flux(q, A, B, C)
        - e1(q, A, B, C, radius, points)
    )


def derivative_F(q: float, h=2.0e-4, radius=26.0, points=700) -> float:
    return float((F(q+h, radius, points)-F(q-h, radius, points))/(2*h))


def derive_prediction(qinf=QINF):
    dv = delta_v(A, B, C)
    sigma = interface_sigma(qinf)
    C_R = np.sqrt(2.0)/(qinf*np.sqrt(dv))
    beta_sigma = 2.0*np.pi*sigma*np.sqrt(C_R)
    fp = derivative_F(qinf)
    alpha_sigma = -beta_sigma/fp
    return {
        "qinf": qinf,
        "DeltaV": dv,
        "sigma": sigma,
        "C_R": float(C_R),
        "beta_sigma": float(beta_sigma),
        "Fprime": float(fp),
        "alpha_sigma": float(alpha_sigma),
    }


def run(outdir="results/v02_validation"):
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    d = derive_prediction()
    rows = []
    for n, qobs in zip(N_VALID, QC_VALID):
        qpred = d["qinf"] + d["alpha_sigma"]/np.sqrt(n)
        observed_shift = qobs-d["qinf"]
        predicted_shift = qpred-d["qinf"]
        rows.append({
            "n": int(n),
            "q_observed": qobs,
            "q_pred_sigma_only": qpred,
            "observed_shift": observed_shift,
            "predicted_shift": predicted_shift,
            "residual": qobs-qpred,
            "fraction_explained": predicted_shift/observed_shift,
        })

    path = out/"sigma_leading_prediction.csv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    summary = out/"sigma_leading_summary.txt"
    summary.write_text("\n".join(f"{k}={v:.16g}" for k,v in d.items())+"\n", encoding="utf-8")

    print("Derived, no-fit coefficient:")
    for k,v in d.items():
        print(f"{k}={v:.12g}")
    print("Validation-only comparison:")
    for r in rows:
        print(r)
    return d, rows


if __name__ == "__main__":
    run()
