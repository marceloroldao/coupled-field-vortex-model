# Mass-ratio reduction of the small-c Bogomolny correction

Status: **derived scaling structure + numerical validation**.

For `c=0`, the charged sector is at the one-component Bogomolny point when

`q_BPS^2 = 2 b`.

The vacuum amplitude and decoupled masses are

`v0^2 = -a/(2b)`,

`m_h^2 = -a`,

`m_X^2 = 2`,

so the natural dimensionless scalar-scale ratio is

`rho_X = m_h^2/m_X^2 = -a/2`.

At small neutral-scalar coupling,

`q_crit^2 = 2b - C(a,b)c^2 + O(c^3)`.

The interface calculation shows that, within numerical precision in the tested domain, `C` is nearly independent of `b` at fixed `a`, consistent with a reduction

`C(a,b) -> C(rho_X)`.

## Numerical collapse tests

At `a=-0.8`, varying `b=0.9,1.0,1.1,1.2,1.3` gives

`C = 2.3702451, 2.3705332, 2.3707738, 2.3709765, 2.3711475`,

with total spread `9.02e-4`, about `3.8e-4` relative.

At `a=-0.9`, varying `b=1.0,1.1,1.2` gives

`C = 2.4112034, 2.4114439, 2.4116447`,

with relative spread about `1.8e-4`.

This is substantially smaller than the variation of `C` when `a` changes.

## Local parametrization

With `rho_X=-a/2`, the currently sampled domain is described locally by

`C(rho_X) ~= 2.03968 + 0.82551 rho_X`,

while a quadratic local approximation is

`C(rho_X) ~= 2.00978 + 0.97899 rho_X - 0.19185 rho_X^2`.

These coefficients are empirical local approximations, not claimed as universal constants.

## Interpretation

The small-`c` correction is controlled primarily by the relative scalar length scales of the decoupled BPS background. The apparent weak `b` dependence in raw parameters largely disappears after expressing the problem in terms of the BPS mass ratio.

Next step: derive the fully rescaled linear-response operator and the corresponding quadratic functional for `C(rho_X)`.