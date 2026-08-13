"""Frozen H-I-J scientific checks for the V0.1 validation campaign.

Acceptance thresholds in this module were fixed before the final full campaign.
They must not be relaxed in response to outcomes.  A numerical nonconvergence
is INCOMPLETE rather than a physics FAIL unless a converged result violates a
pre-declared scientific identity or tolerance.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
import numpy as np
from scipy.integrate import simpson

from validation.core import solve_universal

# Frozen acceptance thresholds.
MAX_LINEAR_C = 2.0e-5
MAX_DIRECT_UNIVERSAL_REL = 5.0e-4       # 0.05 percent
TRUNCATION_SLOPE_MIN = 2.7
TRUNCATION_SLOPE_MAX = 3.3
MAX_BVP_RMS = 5.0e-7
MAX_LINEARIZED_RESIDUAL = 2.0e-5
MAX_B_COLLAPSE = 1.0e-6
MAX_Q_CHARGED = 1.0e-8
MAX_C_REFINEMENT_REL = 2.0e-4


@dataclass(frozen=True)
class UniversalDiagnostics:
    rho_X: float
    C_universal: float
    I_X: float
    I_D: float
    Q_charged: float
    linearized_residual_1: float
    linearized_residual_2: float
    bvp_rms: float
    final_nodes: int
    length: float
    points: int
    tolerance: float

    def to_dict(self) -> dict:
        return asdict(self)


def universal_diagnostics(rho_x: float, *, length: float = 12.0,
                          points: int = 700, tol: float = 2.0e-7,
                          integration_points: int = 30000) -> UniversalDiagnostics:
    """Evaluate the universal coefficient and on-shell BPS identities.

    Definitions:
      r1 = P' + G P + F R
      r2 = R' + 2 F P + 1
      Q_charged = integral [1/2 r1^2 + 1/4 r2^2] dx
      I_X = integral F^2 (1+U) dx
      I_D = integral G^2 F^2 dx
      C = I_X/I_D
    """
    sol = solve_universal(rho_x, length=length, points=points, tol=tol)
    if sol.status != 0:
        raise RuntimeError(sol.message)

    x = np.linspace(-length, length, integration_points)
    F,Fp,G,Gp,P,Pp,R,Rp,U,Up = sol.sol(x)
    r1 = Pp + G*P + F*R
    r2 = Rp + 2.0*F*P + 1.0
    i_x = float(simpson(F*F*(1.0+U), x=x))
    i_d = float(simpson(G*G*F*F, x=x))
    if i_d <= 0.0:
        raise RuntimeError(f"non-positive I_D={i_d}")
    q_ch = float(simpson(0.5*r1*r1 + 0.25*r2*r2, x=x))

    return UniversalDiagnostics(
        rho_X=float(rho_x),
        C_universal=i_x/i_d,
        I_X=i_x,
        I_D=i_d,
        Q_charged=q_ch,
        linearized_residual_1=float(np.max(np.abs(r1))),
        linearized_residual_2=float(np.max(np.abs(r2))),
        bvp_rms=float(np.max(sol.rms_residuals)),
        final_nodes=int(sol.x.size),
        length=float(length),
        points=int(points),
        tolerance=float(tol),
    )


def status_i(diag: UniversalDiagnostics, *, b_collapse: float | None = None) -> str:
    checks = [
        diag.bvp_rms <= MAX_BVP_RMS,
        diag.linearized_residual_1 <= MAX_LINEARIZED_RESIDUAL,
        diag.linearized_residual_2 <= MAX_LINEARIZED_RESIDUAL,
    ]
    if b_collapse is not None:
        checks.append(abs(b_collapse) <= MAX_B_COLLAPSE)
    return "PASS" if all(checks) else "FAIL"


def status_j(diag: UniversalDiagnostics, *, c_refinement_relative: float | None = None) -> str:
    checks = [diag.Q_charged <= MAX_Q_CHARGED, diag.I_D > 0.0]
    if c_refinement_relative is not None:
        checks.append(abs(c_refinement_relative) <= MAX_C_REFINEMENT_REL)
    return "PASS" if all(checks) else "FAIL"


def status_h(*, linear_term: float, C_direct: float, C_universal: float,
             truncation_slope: float | None) -> str:
    if not np.isfinite([linear_term,C_direct,C_universal]).all():
        return "INCOMPLETE"
    if truncation_slope is None or not np.isfinite(truncation_slope):
        return "INCOMPLETE"
    rel = abs(C_direct-C_universal)/abs(C_universal)
    checks = [
        abs(linear_term) <= MAX_LINEAR_C,
        rel <= MAX_DIRECT_UNIVERSAL_REL,
        TRUNCATION_SLOPE_MIN <= truncation_slope <= TRUNCATION_SLOPE_MAX,
    ]
    return "PASS" if all(checks) else "FAIL"


def refinement_relative(values: list[float]) -> float:
    a = np.asarray(values, dtype=float)
    if a.size < 2 or not np.all(np.isfinite(a)):
        return float("nan")
    scale = abs(float(a[-1]))
    if scale == 0.0:
        return float("inf")
    return float(np.ptp(a)/scale)


def loglog_slope(c_values, residuals) -> float:
    c = np.asarray(c_values, dtype=float)
    r = np.abs(np.asarray(residuals, dtype=float))
    mask = np.isfinite(c) & np.isfinite(r) & (c > 0.0) & (r > 0.0)
    if np.count_nonzero(mask) < 3:
        return float("nan")
    return float(np.polyfit(np.log(c[mask]), np.log(r[mask]), 1)[0])
