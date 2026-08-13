# High-winding fusion-boundary scan

Status: **numerical / locally reproduced**  
GitHub Actions reproduction: **pending**

Model point:

- `a = -0.8`
- `b = 1.0`
- `c = 0.4`

Definition:

`Delta_n(q) = E_n(q) - n E_1(q)`

The critical coupling `q_c^(n)` is the root `Delta_n(q)=0` for the axisymmetric winding-`n` vortex.

## Critical couplings

| n | q_c^(n) |
|---:|---:|
| 2 | 1.2859194386 |
| 3 | 1.2843440857 |
| 4 | 1.2836239655 |
| 5 | 1.2832282046 |
| 6 | 1.2829833674 |
| 8 | 1.2827023687 |
| 10 | 1.2825490774 |
| 12 | 1.2824542123 |

The sequence is monotonically decreasing over the tested windings.

## Convergence check for high winding

Roots were recomputed at `(R, points)=(18,400),(22,500),(26,700)`.

| n | q_c @ 18/400 | q_c @ 22/500 | q_c @ 26/700 | max spread |
|---:|---:|---:|---:|---:|
| 8 | 1.2827023768 | 1.2827023687 | 1.2827023623 | 1.46e-8 |
| 10 | 1.2825490893 | 1.2825490774 | 1.2825490714 | 1.78e-8 |
| 12 | 1.2824542349 | 1.2824542123 | 1.2824542066 | 2.84e-8 |

This supports that the observed n-dependence is not a box/grid artifact at the quoted precision.

## Asymptotic extrapolation

Fits over `n={2,3,4,5,6,8,10,12}` give:

- `q_c(n)=q_inf + A/n`: `q_inf ≈ 1.2816491`
- `q_c(n)=q_inf + A/n + B/n^2`: `q_inf ≈ 1.2819518`
- cubic in `1/n`: `q_inf ≈ 1.2820612`

Because the inferred limit depends on fit order, the asymptotic value is classified as **candidate**. The present data support a collective limiting boundary near `q_inf ≈ 1.282`, but more windings and/or an analytic large-n expansion are required before promotion.

## Interpretation

The fusion threshold is not exactly universal in winding number. Nonlinear core physics shifts `q_c^(n)` downward as `n` increases, with an apparent approach to a finite collective limit. This correction is not captured by the simple adiabatic estimate `q_c^2 ≈ 2(b-c^2)`.

Reproduction script: `simulations/qc_high_winding_scan.py`.
