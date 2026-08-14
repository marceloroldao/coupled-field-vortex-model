# V0.2 — Constant-curvature contribution to the finite-winding boundary

## 1. Starting point

For a large circular vortex wall, the V0.2 expansion is

G_wall(R) = 2 pi R sigma + 2 pi A0 + (2 pi K1)/R + O(R^-2),

where A0 is the constant-in-R wall coefficient after the dividing-surface and boundary/ensemble conventions are fixed.

For a flux-n bag at leading order,

R_n = sqrt(C_R n),

with

C_R = sqrt(2)/(q sqrt(DeltaV)).

Dividing the wall energy by n gives

G_wall/n
= 2 pi sigma sqrt(C_R) n^(-1/2)
+ 2 pi A0 n^(-1)
+ (2 pi K1/sqrt(C_R)) n^(-3/2)
+ ... .

Thus the constant-curvature sector produces the coefficient

beta_1 = 2 pi A0

in the large-n energy-per-flux expansion.

## 2. Critical-boundary displacement

Let

F(q) = E_inf(q) - E_1(q),

with

F(q_inf) = 0.

Write the finite-n equality condition as

0 = F(q_n)
  + beta_sigma n^(-1/2)
  + beta_1 n^(-1)
  + O(n^(-3/2)).

Linearizing F around q_inf gives

F(q_n) = F'(q_inf) (q_n-q_inf) + ... .

Therefore

q_n-q_inf
= alpha_sigma n^(-1/2)
+ alpha_1 n^(-1)
+ O(n^(-3/2)),

where

alpha_sigma = -beta_sigma/F'(q_inf)

and the newly derived constant-curvature coefficient is

alpha_1 = -2 pi A0 / F'(q_inf).

This relation contains no giant-vortex fit parameter if A0 is obtained independently from planar-interface data.

## 3. Current numerical implication

The exploratory G2 diagnostics at q_inf gave positive candidate values

A0_candidate ~ 4.5e-4 to 5.8e-4

for the two converged quick domains L=16 and L=14, respectively, while

F'(q_inf) ~ -0.69084.

Hence the predicted alpha_1 is positive, with rough magnitude

alpha_1 ~ 0.004 to 0.005.

This sign is precisely what is required to oppose the negative n^(-1/2) sigma term and can therefore generate a finite-n sign crossover.

The magnitude must still be treated as exploratory because A0 is a cancellation between O(1e-1) moments and has not yet passed a frozen convergence gate.

## 4. Crossover estimate

If

Delta q_n = alpha_sigma n^(-1/2) + alpha_1 n^(-1),

then the two-term sign crossover occurs at

sqrt(n_cross) = -alpha_1/alpha_sigma,

or

n_cross = (alpha_1/alpha_sigma)^2,

provided alpha_sigma and alpha_1 have opposite signs.

Using alpha_sigma ~ -8.03e-4 and alpha_1 ~ 0.004-0.005 gives a rough n_cross of order a few tens. This is consistent in scale with the previously reproduced high-winding sign change between n=32 and n=64, but this comparison is validation-only and must not be used to tune A0.

## 5. Scientific status

DERIVED:

- constant-in-R wall energy produces an n^-1 correction in energy per flux;
- alpha_1 = -2 pi A0/F'(q_inf);
- opposite signs of sigma and A0 naturally allow a finite-winding crossover.

NOT YET ESTABLISHED:

- invariant, converged A0;
- quantitative two-term held-out prediction;
- frozen uncertainty budget;
- robustness away from the reference parameter point.

Therefore this stage is classified INCOMPLETE until A0 convergence and boundary/ensemble closure are demonstrated.

## 6. Impact potential — science and technology

### Science

- **Finite-size scaling of topological defects:** identifies separate geometric origins for n^-1/2 and n^-1 corrections instead of treating them as empirical powers.
- **Superconducting vortex crossover:** provides a mechanism by which moderate-winding vortices can approach the asymptotic boundary from one side while very large vortices approach from the other.
- **Effective interface theory:** links a constant curvature/interface coefficient directly to an observable critical-boundary displacement.
- **Multifield systems:** offers a route to isolate how neutral-field response alters subleading vortex energetics.

### Technology

- **Reduced-order superconducting simulation:** a validated two-term formula could estimate high-winding stability without solving every radial BVP.
- **Flux-management modeling:** the crossover scale may become useful in models of large trapped-flux structures if the theory is later calibrated to real materials.
- **Parameter-screening tools:** independently derived coefficients can reduce computational cost in material/device parameter sweeps.

All technological implications remain conditional on convergence, held-out validation, and experimental/material calibration.
