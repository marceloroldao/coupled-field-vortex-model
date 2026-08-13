# V0.1 Frozen Acceptance Criteria for Blocks H-I-J

These criteria were fixed before the final V0.1 full validation campaign. They are part of the scientific protocol and must not be relaxed after viewing results.

## Block H — small-c critical-boundary displacement

The candidate perturbative law is

`q_crit^2 = 2 b - C(rho_X) c^2 + O(c^3)`.

Required checks:

- `abs(linear_term) <= 2e-5`.
- `abs(C_direct-C_universal)/abs(C_universal) <= 5e-4` (0.05%) for numerically resolved points.
- At the reference point, the log-log slope of the full-solver truncation residual versus `c` must lie in `[2.7, 3.3]`, consistent with `O(c^3)`.
- Solver nonconvergence is `INCOMPLETE`, not automatically a physics `FAIL`.

## Block I — universal response system

For `rho_X = 0.3, 0.4, 0.5`, solve the universal BPS background and response system with the documented finite-box asymptotic conditions.

The linearized first-order identities are

`r1 = P' + G P + F R = 0`,

`r2 = R' + 2 F P + 1 = 0`.

Required checks:

- BVP RMS residual `<= 5e-7`.
- `max(abs(r1)) <= 2e-5`.
- `max(abs(r2)) <= 2e-5`.
- Normalized fixed-`rho_X` profile collapse under changes in `b` must be better than `1e-6` when that collapse test is executed.

## Block J — quadratic Gibbs reduction

Define

`Q_charged = integral [1/2 r1^2 + 1/4 r2^2] dx`,

`I_X = integral F^2 (1+U) dx`,

`I_D = integral G^2 F^2 dx`,

`C_universal = I_X / I_D`.

Required checks:

- `Q_charged <= 1e-8`.
- `I_D > 0`.
- Relative variation of `C_universal` across an adequate refinement sequence `<= 2e-4` when the refinement test is executed.
- The validation report must state the analytic first-order Gibbs/bulk cancellation and the on-shell charged-sector cancellation rather than treating them as empirical fits.

## Required machine-readable fields

The final campaign should record, where applicable:

- `C_direct`
- `C_interface`
- `C_universal`
- `Q_charged`
- `I_X`
- `I_D`
- `linearized_residual_1`
- `linearized_residual_2`
- `truncation_slope`
- individual subtest statuses

No action, normalization, equation, boundary condition, parameter definition, or threshold may be changed merely to convert a scientific failure into a pass.
