# Planar magnetic interface tension

Status: **numerical / locally reproduced**.

Reference parameters: `(a,b,c)=(-0.8,1,0.4)`.

The planar BVP connects the normal core phase `(psi=0,X=1,B=H_c)` to the mixed phase `(psi=v,X=X0,B=0)`, with

- `Delta V = 1/21 = 0.047619047619...`
- `H_c = sqrt(2 Delta V) = 0.308606699924...`.

The Gibbs surface tension changes sign near

`q_sigma = 1.28277880`.

Representative values:

- `sigma(1.2800) = -1.8083e-4`
- `sigma(1.2821745437) = -3.92575e-5`
- `sigma(1.28275) = -1.8704e-6`
- `sigma(1.2830) = +1.4366e-5`
- `sigma(1.2850) = +1.4407e-4`.

Thus the independently derived large-n leading boundary `q_inf=1.2821745437` lies in a regime of **negative planar interface tension**.

## Prediction of the finite-n square-root coefficient

For the large-n bag radius,

`R_n^2 = sqrt(2) n / (q sqrt(Delta V))`, so the wall contribution per flux quantum is

`C(q) n^{-1/2}` with

`C(q)=2 pi sigma(q) sqrt(sqrt(2)/(q sqrt(Delta V)))`.

At `q_inf`, the locally reproduced values are

- `E1(q_inf)=1.51230040395`
- `e_bulk(q_inf)=1.51230040574`
- `F'(q_inf)=d(e_bulk-E1)/dq=-0.690840292`
- `sigma(q_inf)=-3.9257468e-5`
- `C(q_inf)=-5.54550e-4`.

Linearizing the critical condition gives

`q_c^(n)-q_inf ~ A/sqrt(n)`, with

`A_pred = -C/F' = -8.02718e-4`.

The direct giant-vortex fit at high winding gave approximately

`A_num ~ -8.74e-4`.

The planar-interface prediction therefore reproduces the sign and magnitude of the observed asymptotic coefficient to roughly 8% without fitting it to the giant-vortex roots.

Interpretation: the negative `n^{-1/2}` correction is quantitatively attributable to the magnetic Gibbs interface tension. Positive `O(1/n)` curvature/core terms dominate at moderate winding and delay the asymptotic regime.

Reproduction script: `simulations/planar_interface_tension.py`.
