# Large-winding vortex-bag limit

Status: **numerical + analytic, locally reproduced**. GitHub Actions reproduction pending.

Parameters:

- `a = -0.8`
- `b = 1.0`
- `c = 0.4`

## Bag approximation

For large winding `n`, approximate the vortex as a circular core in the `psi=0, X=1` phase embedded in the mixed vacuum. The leading energy is

`E(R) = pi DeltaV R^2 + 2 pi n^2/(q^2 R^2) + 2 pi sigma R + ...`

where `DeltaV = V_core - V_mixed` and `sigma` is the interface tension. The wall term is subleading for `n -> infinity`.

For the parameter point above:

- `V_mixed = -0.297619047619...`
- `V_core = -0.25`
- `DeltaV = 0.047619047619... = 1/21`

Minimizing the leading bulk plus magnetic terms gives

`R_n^2 = sqrt(2) n / (q sqrt(DeltaV))`,

so `R_n ~ sqrt(n)`, and

`E_n/n -> 2 pi sqrt(2 DeltaV)/q`.

## Asymptotic fusion boundary

The large-`n` fusion boundary is estimated by equating the limiting energy per flux quantum to the fully nonlinear numerical `n=1` vortex energy:

`2 pi sqrt(2 DeltaV)/q = E_1(q)`.

Using the same radial solver and normalization as the finite-winding scans gives

`q_c^(infinity) = 1.2821745437`.

At the root, the two energies agree to approximately `5e-12` in the local calculation.

## Comparison with finite winding

The independently computed finite-winding boundaries were

- `q_c^(2) = 1.28591955`
- `q_c^(3) = 1.28434393`
- `q_c^(4) = 1.28362384`
- `q_c^(5) = 1.28322810`
- `q_c^(6) = 1.28298327`
- `q_c^(8) = 1.28270237`
- `q_c^(10) = 1.28254908`
- `q_c^(12) = 1.28245421`

They approach the bag-limit value monotonically from above.

## Interpretation

The winding dependence of the fusion boundary is a finite-core/interface correction. At large `n`, volume and magnetic energies scale as `n`, while the interface contribution scales only as `sqrt(n)`. This explains why the sequence `q_c^(n)` converges to a well-defined collective boundary rather than remaining equal to the pair boundary.

Reproducer: `simulations/large_n_bag_limit.py`.
