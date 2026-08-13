# Finite-winding correction to the collective fusion boundary

Status: **numerical / locally reproduced; asymptotic interpretation candidate**.

For `(a,b,c)=(-0.8,1,0.4)`, use the radial BVP roots

| n | q_c^(n) |
|---:|---:|
|2|1.28591955|
|3|1.28434393|
|4|1.28362384|
|5|1.28322810|
|6|1.28298327|
|8|1.2827023687|
|10|1.2825490774|
|12|1.2824542123|

and the independently derived large-n bag value

`q_inf = 1.2821745437`.

Define `delta_n = q_c^(n)-q_inf`.

## Fits

A free one-power fit `delta_n = A n^{-p}` gives approximately

- `A = 9.888e-3`
- `p = 1.3940`
- RMSE `= 2.07e-5`.

Single fixed powers give RMSE:

- `n^{-1/2}`: `6.96e-4`
- `n^{-1}`: `2.82e-4`
- `n^{-3/2}`: `6.94e-5`
- `n^{-2}`: `3.27e-4`

Thus the currently available finite-n data **do not support a pure `n^{-1/2}` correction**, despite the wall energy itself scaling as `sqrt(n)` in the bag picture. The best single power over `n=2..12` is close to `n^{-1.4}`.

A mixed expansion

`delta_n = A n^{-1/2} + B n^{-1} + C n^{-3/2}`

fits substantially better (RMSE about `4.8e-6`), but the fitted leading `n^{-1/2}` coefficient is small and negative. This indicates strong cancellation and/or that `n<=12` is not yet in the true asymptotic regime.

## Interpretation

The bag derivation proves that the wall contribution to `E_n/n` is naturally `O(n^{-1/2})`, but the critical coupling is defined implicitly by `E_n(q)/n = E_1(q)`. The coefficient of the corresponding shift in `q_c^(n)` can therefore be small or partially cancelled by curvature, profile relaxation, and other finite-core corrections.

Current conclusion: retain `q_inf=1.2821745437` as the independently motivated collective limit, but do **not** claim a verified `1/sqrt(n)` law for `q_c^(n)-q_inf` yet. Larger winding sectors are required.

Reproduction script: `simulations/qc_asymptotic_correction.py`.
