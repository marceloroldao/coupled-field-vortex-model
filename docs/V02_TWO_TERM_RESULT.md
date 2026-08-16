# V0.2 — Independent two-term curvature result

## Result

The independent two-term prediction

q_c^(n) - q_inf = alpha_sigma n^(-1/2) + alpha_1 n^(-1)

was evaluated in GitHub Actions without fitting the validation points.

The independently computed coefficients were

alpha_sigma = -8.028350196e-4,
alpha_1 = +4.132589473e-3,

with candidate crossover

n_cross = (alpha_1/|alpha_sigma|)^2 = 26.50.

The corresponding interface quantities were

sigma = -3.926317007e-5,
A0_candidate = 4.543808968e-4,
F'(q_inf) = -0.6908403057.

## Interpretation

The two terms have opposite signs. Therefore the expansion predicts a finite-winding crossover: the +1/n curvature term dominates first, while the negative 1/sqrt(n) surface-tension term decays more slowly and eventually dominates.

The radial data remain positive through n=32 and become negative by n=64. The independent two-term model predicts the sign change somewhat earlier, near n≈26.5. It therefore captures the existence and approximate scale of the crossover, but not yet its precise location.

The absolute residual decreases strongly with winding:

- n=16: about 1.13e-4
- n=32: about 4.61e-5
- n=64: about 1.97e-5
- n=128: about 8.80e-6

This decreasing residual is consistent with, but does not prove, the presence of a next asymptotic term.

## Scientific classification

**What succeeded:**

- the sign competition is predicted independently;
- the asymptotic negative high-n side is recovered;
- the crossover scale is predicted within the correct order of magnitude;
- residuals shrink substantially as n increases.

**What did not yet succeed:**

- the two-term formula does not quantitatively reproduce moderate winding;
- the predicted crossover occurs too early;
- A0 is still a candidate coefficient because its full invariant/boundary accounting is not closed.

Accordingly, G3 is **PARTIAL / INCOMPLETE**, not PASS.

## Next test

If the next wall-energy term is

(2 pi K1)/R,

then after division by n and using R~sqrt(n), the induced critical-boundary correction scales as n^(-3/2). The next diagnostic is therefore to test whether

[q_observed - q_two-term] n^(3/2)

approaches a constant at high n. This is only a scaling diagnostic; K1 must still be derived independently before any third-term coefficient can be claimed predictive.

## Impact potential — science and technology

### Science

A successful hierarchy linking sigma, A0, and K1 to n^(-1/2), n^(-1), and n^(-3/2) would provide a controlled local-interface interpretation of finite-winding giant-vortex corrections. This could be useful in superconducting vortex theory, topological-defect asymptotics, multifield interfaces, and finite-size scaling near critical couplings.

### Technology

If later validated against experimentally relevant superconductors, such an asymptotic hierarchy could reduce the computational cost of large-flux vortex simulations and support faster parameter scans for trapped-flux stability, vortex engineering, and superconducting-device modeling. These implications remain conditional on full G2-G5 validation and material calibration.
