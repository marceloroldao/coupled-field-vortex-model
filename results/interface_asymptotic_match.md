# Interface-to-giant-vortex asymptotic matching

Status: **numerical / locally reproduced; quantitative asymptotic match**.

At `(a,b,c)=(-0.8,1,0.4)`, the independently derived bag-limit crossing is

`q_inf = 1.2821745437`.

The planar Gibbs interface calculation gives at this same coupling

`sigma(q_inf) = -3.925746789433e-05`.

For the leading bag radius `R_n = r0 sqrt(n)`, the wall contribution to energy per flux is

`C/sqrt(n)`, with

`C = 2*pi*sigma*r0`.

Linearizing the criticality condition

`e_bulk(q_c) - E1(q_c) + C/sqrt(n) + ... = 0`

around `q_inf` gives

`q_c^(n)-q_inf = A/sqrt(n)+...`,

where

`A = -C / d_q[e_bulk-E1]`.

Using the independently computed derivative

`d_q[e_bulk-E1] = -0.690840291982292`

gives

`A_pred = -8.02718e-4`.

The earlier direct high-winding fit gave approximately

`A_num ~ -8.74e-4`.

Thus the interface calculation predicts the sign and magnitude of the leading high-winding correction to within about 8 percent without fitting A to the giant-vortex roots.

Fixing `A=A_pred`, the `n=32,64,128` data imply a next positive `B/n` contribution with pointwise B estimates around `0.00526--0.00561` (mean `0.00542`). Allowing an additional `C/n^(3/2)` term reduces the three-point residual to about `4.4e-8`.

Interpretation: the negative planar interface tension explains the eventual approach of `q_c^(n)` from below at very large winding, while positive curvature/profile-relaxation corrections dominate at moderate winding and produce the observed crossing between `n=32` and `n=64`.

Reproduction: `simulations/interface_asymptotic_match.py`.
