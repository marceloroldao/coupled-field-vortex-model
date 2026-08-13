# On-shell quadratic response identity near the Bogomolny point

Status: **derived + numerically verified**.

For small neutral-scalar coupling, write

`X = 1 + c eta + O(c^2)`.

At `c=0`, the charged sector is evaluated on the one-component BPS interface. The first-order neutral response satisfies

`(-d_z^2 + 2) eta = -2 |psi_BPS|^2`,

with asymptotic conditions `eta(-infinity)=0` in the normal phase and `eta(+infinity)=-v0^2` in the broken phase.

The quadratic neutral-response functional before thermodynamic bulk subtraction is

`F2[eta] = integral dz [ 1/2 (eta')^2 + eta^2 + 2 eta |psi_BPS|^2 ]`.

Multiplying the response equation by `eta`, integrating by parts, and using the asymptotic boundary conditions gives the on-shell identity

`F2_on-shell = integral dz eta |psi_BPS|^2 + boundary term`.

The finite-box boundary term vanishes exponentially as the computational domain is enlarged. Local numerical checks gave discrepancies between the two sides of order `10^-7` or smaller for representative parameter points.

This identity is useful because it collapses the gradient-dependent quadratic functional to a source-response overlap. It is not yet the full coefficient controlling the critical-coupling shift: the complete Gibbs expansion must also include bulk-energy subtraction, the expansion of the thermodynamic critical field, and charged-sector relaxation along the BPS family.

For the v0.1 manuscript, the target form remains

`q_crit^2 = 2 b - C(rho_X) c^2 + O(c^3)`,

with `rho_X = m_h^2/m_X^2`, and `C(rho_X)` to be defined by the fully bulk-subtracted on-shell Gibbs functional rather than by an empirical fit.