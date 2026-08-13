# Neutral-scalar perturbation around the Bogomolny point

Status: **derived + numerical cross-check**.

For `c=0` the neutral scalar decouples and the charged sector has the Bogomolny point

`q_BPS^2 = 2 b`.

Write the neutral field for small coupling as

`X = 1 + c eta + O(c^2)`.

The static Euler-Lagrange equation

`-∇^2 X + (-1 + X^2 + 2 c |psi|^2) X = 0`

then gives the linear response equation on the `c=0` background

`(-∇^2 + 2) eta = -2 |psi_0|^2`.

The bulk boundary condition follows from the exact mixed vacuum,

`X_0^2=(b+a c)/(b-c^2)`,

so `eta_bulk=a/(2b)=-v_0^2`, consistent with the response equation far inside the broken phase.

Direct small-c numerical tests at `(a,b)=(-0.8,1.0)` show

`q_crit^2 - 2b = O(c^2)`

with no resolved linear term.  For `c=0.02...0.18`, `(q_crit^2-2b)/c^2` stays near `-2.3`.

A stronger perturbative cross-check predicts this coefficient without fitting the critical roots.  At fixed `q_BPS=sqrt(2b)`, the interfacial tension behaves as

`sigma(c,q_BPS) = K2 c^2 + K3 c^3 + ...`

with the locally reproduced fit

`K2 = 0.11598357495`.

Independently,

`∂ sigma / ∂(q^2) |_(c=0,q_BPS) = 0.04903456986`.

Linearizing the condition `sigma=0` gives

`delta(q_crit^2) = -(K2 / sigma_{q^2}) c^2 + ...`,

hence

`q_crit^2 = 2b - 2.36534 c^2 + O(c^3)`

for this `(a,b)` point.

The direct critical-root scan gives a coefficient close to `-2.33`, so the independent perturbative prediction agrees at the percent level.

Interpretation: the neutral scalar shifts the Bogomolny/type-I–type-II boundary first at quadratic order in the inter-field coupling for this regular perturbative branch.  The naive adiabatic replacement `b -> b-c^2`, which would give coefficient `-2`, misses the additional contribution from the spatially varying neutral-scalar response across the interface.
