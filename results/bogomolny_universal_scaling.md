# Universal scaling of the small-c Bogomolny correction

Status: **numerical / locally reproduced; analytic reduction in progress**.

Near the decoupled Bogomolny point `c=0`, write

`q_crit^2 = 2 b - C c^2 + O(c^3)`.

Define the interfacial expansion at fixed `q_BPS^2=2b`,

`sigma(c,q_BPS) = K2 c^2 + O(c^3)`,

and

`D = (partial sigma / partial(q^2))_{c=0,q=q_BPS}`.

Then

`C = K2 / D`.

## Numerical scaling test

At fixed `a=-0.8` and varying `b`:

| b | K2 | b^2 K2 | D | b^2 D | C |
|---:|---:|---:|---:|---:|---:|
|0.90|0.143486285|0.116223891|0.060536475|0.049034545|2.370245116|
|1.00|0.116238016|0.116238016|0.049034545|0.049034545|2.370533194|
|1.10|0.096074226|0.116249814|0.040524417|0.049034545|2.370773795|
|1.20|0.080735940|0.116259753|0.034051767|0.049034545|2.370976497|
|1.30|0.068797714|0.116268136|0.029014524|0.049034545|2.371147461|

At fixed `a=-0.9`:

| b | K2 | b^2 K2 | D | b^2 D | C |
|---:|---:|---:|---:|---:|---:|
|1.00|0.141079788|0.141079788|0.058510114|0.058510114|2.411203448|
|1.10|0.116606492|0.141093855|0.048355466|0.058510114|2.411443868|
|1.20|0.097990004|0.141105606|0.040632023|0.058510114|2.411644705|

The data show, to current numerical accuracy,

`K2(a,b) ~ kappa(a)/b^2`,

and

`D(a,b) ~ delta(a)/b^2`.

Therefore the ratio

`C(a,b)=K2/D`

is independent of `b` at this order, up to the residual numerical/finite-c fitting error.

## Mass-ratio form

At `c=0`,

`m_h^2=-a`, `m_X^2=2`,

so the remaining dimensionless control parameter can be written

`rho_X = m_h^2/m_X^2 = -a/2`.

This supports the reduced perturbative form

`q_crit^2 = 2b - C(rho_X)c^2 + O(c^3)`.

## Linear neutral response

Writing `X=1+c eta+O(c^2)` gives

`(-d_z^2+2) eta = -2 |psi_BPS|^2`,

with asymptotic conditions `eta(-infinity)=0` and `eta(+infinity)=-v0^2` for the planar interface convention used here.  Normalizing `eta` by `v0^2` collapses profiles with the same `a` and different `b` to numerical precision, consistent with the scaling above.

## Caution

The neutral-sector quadratic density alone is not the full `K2`: thermodynamic bulk subtraction, the `H_c(c)` shift, and relaxation of the charged BPS family must be treated consistently.  The next analytic step is to derive the complete on-shell second-order Gibbs interfacial functional before identifying an exact integral representation for `C(rho_X)`.
