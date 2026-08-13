# Analytic reduction of the zero-interface boundary

Status: **derived + numerical pattern; interpretation candidate**.

For the mixed vacuum of

`V = a|psi|^2 + b|psi|^4 + c|psi|^2 X^2 - X^2/2 + X^4/4`,

with

`D = b-c^2`,

`v^2 = -(a+c)/(2D)`,

`X0^2 = (b+ac)/D`,

the bulk free-energy density difference between the normal phase `(psi=0,X=1)` and the mixed phase is exactly

`DeltaV = (a+c)^2/[4(b-c^2)]`.

Hence the thermodynamic critical field in the present normalization is

`H_c = |a+c|/sqrt[2(b-c^2)]`.

This shows that the interface problem depends strongly on the combinations `a+c` and `b-c^2` rather than on `(a,b,c)` independently.

A second numerical pattern appears on the computed `sigma=0` boundary. Across seven independently located points, the combination

`q_inf * v`

is nearly constant:

mean `0.70693`, standard deviation `0.00272`, compared with `1/sqrt(2)=0.70710678`.

Equivalently, in the gauge-mass convention `m_A = sqrt(2) q v`, the zero-interface boundary lies close to

`m_A ~ 1`.

Thus a compact candidate condition is

`q_inf^2 ~ (b-c^2)/[-(a+c)]`.

Across the seven current zero-interface points, this relation is satisfied at roughly the percent level or better (maximum relative deviation about 1.3 percent in q^2 for this limited set).

This provides a plausible explanation for why the numerically determined surface `c_*(a,b)` looks nearly affine over the scanned region: the exact vacuum reduction collapses the dependence to simple rational combinations, while `q_inf v ~ 1/sqrt(2)` supplies an approximately constant spectral condition.

This is not yet claimed as an exact Bogomolny relation. The neutral scalar changes the interface profile and the scalar normal modes are mixed, so the conventional single-component GL critical-coupling argument does not transfer automatically. The correct next test is to map the residual of

`R = q_inf^2[-(a+c)]/(b-c^2) - 1`

over a wider zero-interface data set and determine whether it tends systematically to zero or merely remains small locally.
