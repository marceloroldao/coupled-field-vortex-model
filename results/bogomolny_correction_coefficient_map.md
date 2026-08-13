# Perturbative correction coefficient C(a,b)

Status: **numerical / locally reproduced; perturbative classifier candidate**.

Near the decoupled Bogomolny limit `c=0`, write

`q_crit^2 = 2 b - C(a,b) c^2 + O(c^3)`.

Instead of fitting `q_crit` directly, estimate `C` from independent interface quantities:

`C = K2 / (d sigma / d(q^2))`,

where

`sigma(c,q_BPS) = K2 c^2 + O(c^3)`

at `q_BPS^2=2b`.

Locally reproduced values:

| a | b | K2 | d sigma/d(q^2) | C |
|---:|---:|---:|---:|---:|
| -0.60 | 0.90 | 0.089895 | 0.039320 | 2.286260 |
| -0.70 | 1.00 | 0.093463 | 0.040134 | 2.328776 |
| -0.80 | 1.00 | 0.116238 | 0.049035 | 2.370529 |
| -0.90 | 1.10 | 0.116606 | 0.048355 | 2.411442 |
| -1.00 | 1.20 | 0.116655 | 0.047589 | 2.451304 |
| -0.80 | 1.20 | 0.080735 | 0.034052 | 2.370962 |

A notable feature is the weak dependence on `b` at fixed `a`: changing `b` from `1.0` to `1.2` at `a=-0.8` changes `C` by less than `5e-4`.

Over the present domain, an empirical local fit in `a` alone is

`C(a) ≈ 2.03968 - 0.41275 a`,

with RMSE about `8.3e-4`.

A quadratic fit

`C(a) ≈ 2.00978 - 0.48950 a - 0.04796 a^2`

reduces the in-sample RMSE to about `1.5e-4`, but should not yet be interpreted as an analytic law.

Interpretation: the leading neutral-scalar correction to the Bogomolny coupling appears to be controlled primarily by the quadratic charged-scalar parameter `a`, with only weak dependence on `b` in the tested neighborhood.  Further derivation from the linear-response Green function is required before promoting this to a formula.
