"""Analytic/numeric checks for the coupled-field mixed phase.

This script reproduces the first local validation suite performed outside
GitHub Actions. It scans the stable mixed phase and verifies:

1. the Hessian determinant identity
   det(M_s^2) = 4 v^2 X0^2 (b - c^2)
2. the approximate molecular-window ordering
   q_LR = m_-/v < q_c = sqrt(2 (b-c^2))

The second relation is an approximate classifier because q_c comes from the
adiabatic reduction. It is recorded as a candidate relation, not an exact
nonlinear vortex theorem.
"""

from __future__ import annotations

import math
import numpy as np


def mixed_vacuum(a: float, b: float, c: float):
    D = b - c * c
    if D <= 1e-12:
        return None
    v2 = -(a + c) / D
    x2 = (b + a * c) / D
    if v2 <= 1e-12 or x2 <= 1e-12:
        return None
    return math.sqrt(v2), math.sqrt(x2)


def mixed_masses(a: float, b: float, c: float):
    vacuum = mixed_vacuum(a, b, c)
    if vacuum is None:
        return None
    v, x0 = vacuum
    matrix = 2.0 * np.array(
        [[b * v * v, c * v * x0], [c * v * x0, x0 * x0]], dtype=float
    )
    eigenvalues = np.linalg.eigvalsh(matrix)
    if eigenvalues[0] <= 1e-10:
        return None
    return math.sqrt(eigenvalues[0]), math.sqrt(eigenvalues[1]), v, x0, matrix


def run_scan():
    valid = 0
    violations = 0
    max_det_relative_error = 0.0
    min_window = float("inf")
    max_window = -float("inf")

    for a in np.linspace(-2.0, 0.5, 81):
        for b in np.linspace(0.1, 2.0, 61):
            for c in np.linspace(-1.2, 1.2, 61):
                result = mixed_masses(a, b, c)
                if result is None:
                    continue
                m_minus, m_plus, v, x0, matrix = result
                D = b - c * c

                det_numeric = float(np.linalg.det(matrix))
                det_expected = 4.0 * v * v * x0 * x0 * D
                relative_error = abs(det_numeric - det_expected) / max(
                    1e-12, abs(det_expected)
                )
                max_det_relative_error = max(max_det_relative_error, relative_error)

                q_lr = m_minus / v
                q_c = math.sqrt(2.0 * D)
                window = q_c - q_lr
                min_window = min(min_window, window)
                max_window = max(max_window, window)
                if q_lr > q_c + 1e-10:
                    violations += 1
                valid += 1

    return {
        "valid_points": valid,
        "ordering_violations": violations,
        "max_det_relative_error": max_det_relative_error,
        "min_q_window": min_window,
        "max_q_window": max_window,
    }


if __name__ == "__main__":
    ref = mixed_masses(-0.8, 1.0, 0.4)
    assert ref is not None
    m_minus, m_plus, v, x0, _ = ref
    print(
        "reference:",
        {"m_minus": m_minus, "m_plus": m_plus, "v": v, "X0": x0},
    )
    print("scan:", run_scan())
