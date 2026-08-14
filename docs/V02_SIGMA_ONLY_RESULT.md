# V0.2 — Sigma-only no-fit result

## Status

The first parameter-free finite-winding prediction based only on the planar surface tension has been executed in GitHub Actions.

The derived coefficient was

alpha_sigma = -8.02835020009e-4,

from

sigma = -3.92631700839e-5,
F'(q_inf) = -0.690840305657,
C_R = 5.0544917565.

The leading prediction is

q_c^(n) - q_inf = alpha_sigma n^(-1/2).

## Result on n = 2...12

The observed finite-winding roots lie above q_inf, while the sigma-only term predicts a negative shift. Therefore the sigma-only model is classified as **FAIL for the pre-asymptotic n=2...12 regime**.

This is a scientific result, not a numerical failure of the workflow.

The mismatch grows in relative sign significance with n over this limited range, which means subleading terms cannot be omitted there.

## High-winding evidence already present in the repository

The previously reproduced high-winding roots are:

- n=16: q_c=1.2823450021208787
- n=20: q_c=1.2822856180749810
- n=24: q_c=1.2822490744391220
- n=32: q_c=1.2822078277947904
- n=64: q_c=1.2821584946080210
- n=128: q_c=1.2821446722518808

with q_inf=1.2821745437.

These data cross from q_c>q_inf to q_c<q_inf between n=32 and n=64.

That sign reversal is qualitatively consistent with the independently derived negative n^(-1/2) surface-tension contribution eventually becoming dominant at sufficiently large winding.

A two-term descriptive fit of the high-n data to

Delta q_n = A n^(-1/2) + B n^(-1)

gives approximately

A = -9.3929e-4,
B = 6.4418e-3.

The fitted leading coefficient has the same sign and comparable magnitude to the independently predicted

alpha_sigma = -8.0284e-4.

This comparison is validation-only: alpha_sigma was obtained before using the high-n roots.

## Interpretation

The current evidence supports a crossover picture:

1. moderate winding is dominated by positive subleading finite-size terms;
2. the negative surface-tension n^(-1/2) term becomes increasingly important with n;
3. at sufficiently high winding the total shift changes sign and approaches q_inf from below.

This is not yet promoted to a final V0.2 claim because the positive subleading coefficient must still be derived independently rather than fitted.

The natural next target is the constant wall/curvature sector A0, expected to generate an n^(-1) contribution to q_c^(n)-q_inf.

## Impact potential — science and technology

### Science

- Provides evidence for a genuine finite-winding crossover rather than a single-power approach to the asymptotic critical boundary.
- Distinguishes the asymptotic surface-tension contribution from pre-asymptotic curvature/interface corrections.
- Offers a falsifiable route to connect planar interface physics with giant-vortex spectra in multicomponent superconducting models.
- May clarify why moderate-winding data can appear to approach an asymptote from the opposite side from the true leading large-n correction.

### Technology

If later calibrated to real superconducting systems, a controlled multi-term finite-winding expansion could improve reduced models for large trapped-flux structures, giant-vortex stability, and fast parameter scans in superconducting-device simulation.

These technological implications remain conditional on independent derivation of the subleading coefficient and later experimental/material calibration.
