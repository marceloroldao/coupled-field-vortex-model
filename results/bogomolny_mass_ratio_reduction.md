# Mass-ratio reduction of the small-c Bogomolny correction

Status: **derived scaling + numerical support**.

At `c=0`, the neutral scalar decouples and the charged sector is the one-component Abelian-Higgs/Ginzburg-Landau model at the Bogomolny point `q_BPS^2=2b`.

The decoupled vacuum has

`v0^2 = -a/(2b)`.

In the normalization used in this repository, the charged-amplitude mass and neutral-scalar mass at `c=0` are

`m_h^2 = 2 b v0^2 = -a`,

`m_X^2 = 2`.

Therefore the natural dimensionless scale ratio controlling the neutral response around the BPS background is

`rho_X = m_h^2/m_X^2 = (-a)/2`.

This explains why the perturbative coefficient in

`q_crit^2 = 2b - C(a,b)c^2 + O(c^3)`

was observed to depend very weakly on `b` at fixed `a`: after rescaling distances by the charged-amplitude length, the relative neutral correlation length is controlled by `rho_X`, not by `b` separately.

For the locally reproduced points

| a | b | C |
|---:|---:|---:|
| -0.60 | 0.90 | 2.286260 |
| -0.70 | 1.00 | 2.328776 |
| -0.80 | 1.00 | 2.370529 |
| -0.90 | 1.10 | 2.411442 |
| -1.00 | 1.20 | 2.451304 |
| -0.80 | 1.20 | 2.370962 |

the two points with identical `a=-0.8` but different `b` differ in `C` by only `4.33e-4`.

A local linear representation in the physical ratio `rho_X=(-a)/2` is

`C(rho_X) ~= 2.039676 + 0.825508 rho_X`,

with RMSE about `8.3e-4` over the current sample. A quadratic local representation is

`C(rho_X) ~= 2.009779 + 0.978990 rho_X - 0.191853 rho_X^2`,

with RMSE about `1.5e-4`.

These polynomial coefficients are descriptive, not claimed as universal constants. The structural result is the reduction from an apparent two-parameter dependence `C(a,b)` to a dependence dominated by the mass ratio `m_h^2/m_X^2` in the small-c expansion.

Next step: derive the dimensionless linear-response boundary-value problem explicitly after the BPS rescaling, and test whether `C` is exactly a functional of `rho_X` alone at order `c^2`.
