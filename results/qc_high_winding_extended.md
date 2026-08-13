# Extended high-winding fusion-boundary scan

Status: **numerical / locally reproduced; asymptotic interpretation candidate**.

Using the same coupled-field radial BVP, with a bag-profile initial guess for giant vortices, the fusion boundary `Delta_n(q)=E_n-nE_1=0` was extended to high winding.

| n | q_c^(n) |
|---:|---:|
|16|1.2823450021208787|
|20|1.2822856180749810|
|24|1.2822490744391220|
|32|1.2822078277947904|
|64|1.2821584946080210|
|128|1.2821446722518808|

The independent leading-order bag value is

`q_inf = 1.2821745437`.

The sequence crosses this leading value between `n=32` and `n=64`. Tightened BVP tolerances and larger boxes confirm the crossing; it is not explained by the previously tested finite-domain error.

For the high-n tail, a two-term form

`q_c^(n)-q_inf = A n^{-1/2} + B n^{-1}`

is strongly supported. Fitting the highest-winding points gives approximately

- `A ~= -8.7e-4`
- `B ~= +6.0e-3`

with sub-micro-level RMS residual on `n=32,64,128`.

Interpretation: the expected `n^{-1/2}` surface contribution does appear asymptotically, but its effective coefficient is negative. A positive `1/n` curvature/core correction dominates at moderate winding, which is why scans only through `n<=12` misleadingly suggested a faster positive power law.

This does **not** invalidate the leading bag energy. It indicates that the next-order interfacial contribution to the giant-vortex energy has nontrivial sign in this coupled-field model. The next theoretical task is to compute the planar magnetic-interface tension directly and compare its sign and magnitude with the fitted `A` coefficient.

Reproduction/analysis helper: `simulations/qc_high_winding_extended.py`.
