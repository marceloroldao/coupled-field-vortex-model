# Small-c correction around the Bogomolny limit

Status: **numerical / locally reproduced; perturbative interpretation candidate**.

At `c=0`, the neutral scalar decouples and the charged sector recovers the one-component Abelian-Higgs / Ginzburg-Landau critical condition

`q_BPS^2 = 2 b`.

For small nonzero `c`, the vacuum quantities expand as

`v^2 = -a/(2b) - c/(2b) - a c^2/(2b^2) + O(c^3)`

and

`X_0^2 = 1 + (a/b)c + c^2/b + O(c^3)`.

A naive adiabatic reduction suggests

`q_crit^2 ~ 2(b-c^2)`,

but the numerically determined `sigma=0` surface shows an additional correction of order a few percent for moderate `c`.

Across the current nine sigma-zero points, the quantity

`delta q^2 = q_crit^2 - 2b`

is dominated by a quadratic dependence on `c`. A one-term fit `delta q^2 = K c^2` gives `K ~ -2.276` with RMSE ~ `1.1e-3`.

A low-order three-feature fit

`delta q^2 = A c + B a c + C c^2`

gives approximately

- `A = 0.22017`
- `B = 0.44276`
- `C = -1.81500`

with RMSE ~ `1.5e-4` over the current sample.

This fit is descriptive, not yet a derived perturbation series. The absence of a large pure-linear `c` trend and the strong quadratic contribution are consistent with the expectation that the leading Bogomolny shift is dominated by second-order backreaction of the neutral scalar, while profile relaxation can generate smaller parameter-dependent corrections.

The next analytic task is to compute the first nonvanishing correction to the planar interface energy by solving the linearized neutral-scalar response on the BPS background, rather than fitting the finite-c surface directly.
