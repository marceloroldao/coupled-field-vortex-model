# V0.2 G1/G3 — Fixed-flux matching and curvature scaling

## Purpose

The planar interface calculation is naturally formulated in a Gibbs ensemble at the thermodynamic critical field Hc, while an n-vortex has fixed quantized magnetic flux. This note derives the leading bridge between those ensembles and identifies the asymptotic scaling of finite-winding corrections without fitting giant-vortex data.

## 1. Fixed-flux bag energy

For a large n-vortex approximated by a normal core of radius R surrounded by the mixed vacuum, the quantized flux is

Phi_n = 2 pi n / q.

If the magnetic field in the core is approximately uniform,

B_in pi R^2 = Phi_n,

so

B_in = 2 n / (q R^2).

Let

DeltaV = V_normal - V_mix > 0.

The leading fixed-flux energy is

E0(R;n,q) = pi DeltaV R^2 + 2 pi n^2/(q^2 R^2).

Including the independently computed planar wall sector gives the asymptotic organization

E(R;n,q) = E0(R;n,q) + 2 pi sigma(q) R + 2 pi A0(q) + 2 pi K1(q)/R + O(R^-2).

Here sigma is the planar Gibbs surface tension. A0 and K1 denote curvature/dividing-surface sectors and must be obtained independently from planar response, not fitted to radial-vortex data.

## 2. Leading radius and critical field

Minimizing E0 gives

DeltaV R0^4 = 2 n^2/q^2,

therefore

R0^2 = sqrt(2) n/(q sqrt(DeltaV)).

The corresponding interior field is

B0 = 2 n/(q R0^2) = sqrt(2 DeltaV).

But the thermodynamic critical field of the two homogeneous phases satisfies

Hc^2 = 2 DeltaV.

Hence

B0 = Hc.

This equality is the leading ensemble bridge: the fixed-flux large-n bag self-selects the same bulk magnetic field used by the planar Gibbs interface calculation.

## 3. First radius correction from nonzero surface tension

Write

R = R0 + deltaR.

The second derivative of E0 at R0 is

E0''(R0) = 8 pi DeltaV.

At first order in sigma,

0 = E'(R0 + deltaR)
  = E0''(R0) deltaR + 2 pi sigma + ...,

so

deltaR_sigma = - sigma/(4 DeltaV).

The induced shift of the interior magnetic field is

B_in = 2n/(qR^2)
     = Hc - 2 Hc deltaR/R0 + ...,

therefore

B_in - Hc = sigma/(Hc R0) + ... .

Thus a nonzero planar tension produces an O(R0^-1) = O(n^-1/2) correction to the interior field.

## 4. Energy per flux and finite-n hierarchy

At the leading stationary radius,

E0(R0)/n = 2 pi Hc/q.

The perimeter contribution per flux quantum scales as

[2 pi sigma R0]/n ~ n^-1/2.

The constant curvature sector contributes

[2 pi A0]/n ~ n^-1.

The 1/R curvature sector contributes

[2 pi K1/R0]/n ~ n^-3/2.

Therefore a parameter-free asymptotic expansion of the energy per flux must have the hierarchy

E_n/n = E_infinity
      + alpha_1/2 n^-1/2
      + alpha_1 n^-1
      + alpha_3/2 n^-3/2
      + ...,

with coefficients derived from sigma, A0, K1 and the q-dependence of the bulk quantities.

## 5. Consequence for finite-winding critical couplings

Define q_c^(n) by the crossing

E_n(q)/n = E_1(q),

and q_c^(infinity) by

E_infinity(q)/1 = E_1(q).

If

F(q) = E_infinity(q) - E_1(q)

has nonzero derivative at q_c^(infinity), then linearizing gives

q_c^(n) - q_c^(infinity)
= - delta e_n(q_c^(infinity)) / F'(q_c^(infinity)) + ...,

where delta e_n is the finite-n correction to E_n/n.

Hence the same powers n^-1/2, n^-1, n^-3/2, ... propagate into the finite-winding critical-coupling shift unless a lower-order coefficient vanishes or is anomalously small.

This gives a falsifiable diagnostic:

- nonzero sigma(q_c^infinity) generically implies an n^-1/2 leading shift;
- if sigma is zero or strongly suppressed, A0 can make n^-1 leading;
- if both sigma and A0 vanish/suppress, K1 can expose n^-3/2 behavior.

No exponent should be selected from a numerical fit before independently evaluating these coefficients.

## 6. Boundary/ensemble closure

The first variation of the planar Gibbs functional produces boundary terms

[2 f0' f1 + X0' X1 + (h0' - Hc) h1]_{-infinity}^{+infinity}.

For bulk-preserving perturbations with

f1 -> 0,
X1 -> 0,
h1 -> 0

in the superconducting exterior and h0' -> Hc on the normal side, these terms vanish.

However, the fixed-flux problem permits an O(1/R) shift of the interior field when sigma != 0. That shift is already accounted for by minimizing the fixed-flux bag energy rather than by silently imposing B_in = Hc at every order.

This separation prevents double counting: planar response determines wall coefficients, while fixed-flux minimization determines the radius/interior-field adjustment.

## 7. Current status

DERIVED:

- leading fixed-flux/Gibbs ensemble bridge B0 = Hc;
- first radius shift deltaR_sigma = -sigma/(4 DeltaV);
- interior-field shift B_in-Hc = sigma/(Hc R0) + ...;
- finite-n energy-per-flux hierarchy n^-1/2, n^-1, n^-3/2;
- corresponding hierarchy for q_c^(n)-q_c^(infinity) when F'(q_c^infinity) != 0.

STILL TO TEST:

- numerical values and convergence of sigma, A0 and later K1 at q_c^infinity;
- whether any lower-order coefficient is actually suppressed in the reference model;
- held-out large-n radial predictions.

G1 is now analytically closed at the leading fixed-flux matching level, while G2/G3 remain open numerically.

## 8. Impact potential — science and technology

### Science

- **Finite-size scaling of vortices:** the derivation predicts which powers of winding number should appear and ties each power to a distinct physical interface coefficient.
- **Type-I/type-II crossover:** it separates surface-tension effects from genuinely curvature-driven effects near the Bogomolny boundary.
- **Ensemble consistency:** it gives a clean bridge between Gibbs-interface calculations and fixed-flux topological sectors, reducing a common source of mismatched comparisons.
- **Topological-defect asymptotics:** the same logic applies to bubbles, flux tubes and other defects with a conserved charge/flux and a curved interface.

### Technology

- **Fast superconducting-vortex estimators:** if G2-G5 validate the coefficients, large-n energies and critical boundaries can be estimated without a full nonlinear radial solve for every n.
- **Flux-trapping analysis:** finite-size corrections can improve models of when large trapped-flux structures split or merge.
- **Reduced-order simulation:** separating n^-1/2, n^-1 and n^-3/2 contributions can support compact surrogate models for parameter optimization in superconducting-device simulations.

All device/material implications remain conditional on later experimental calibration and are not claims of demonstrated engineering performance.
