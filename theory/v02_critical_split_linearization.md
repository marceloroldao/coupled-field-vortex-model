# V0.2 — Linearized relation for planar/large-n critical splitting

## Purpose

This note derives a parameter-free local consistency relation between the planar zero-tension point q_sigma and the independently determined large-n critical root q_inf.

The aim is not to assume that q_sigma != q_inf, but to determine what numerical signatures must agree if a small split is real.

## 1. Definitions

Let

sigma(q_sigma) = 0

be the planar-interface zero-tension condition, and let q_inf denote the independently obtained large-n critical root.

Define

Delta q = q_sigma - q_inf.

If |Delta q| is small and sigma(q) is smooth with nonzero first derivative in the interval, Taylor expansion about q_sigma gives

sigma(q_inf)
= sigma(q_sigma) + sigma'(q_sigma)(q_inf-q_sigma)
  + 1/2 sigma''(xi)(q_inf-q_sigma)^2

for some xi between q_inf and q_sigma.

Since sigma(q_sigma)=0,

sigma(q_inf)
= -sigma'(q_sigma) Delta q
  + O(Delta q^2).

Therefore

Delta q
= - sigma(q_inf)/sigma'(q_sigma)
  + O(Delta q^2).

This relation contains only planar-interface quantities plus the independently frozen q_inf.

## 2. Independent consistency test

A genuine small critical split must satisfy two numerically independent determinations:

1. root difference

Delta q_root = q_sigma - q_inf;

2. local linear prediction

Delta q_lin = -sigma(q_inf)/sigma'(q_sigma).

The comparison

R_split = Delta q_lin / Delta q_root

should approach 1 as domain, mesh, and solver tolerances are refined, provided the split is resolved and the quadratic remainder is negligible.

This test is stronger than merely observing sigma(q_inf) != 0.

## 3. Derivative extraction

sigma'(q_sigma) must be obtained without finite-n giant-vortex data. Admissible routes are:

- centered finite differences around q_sigma with step-size convergence;
- local polynomial fit using only planar sigma(q) samples;
- a variational derivative of the on-shell interface functional if derived independently.

The V0.2 numerical implementation should record sigma'(q_sigma) for multiple dq values and verify a stable plateau before using Delta q_lin.

## 4. Error structure

Let epsilon_sigma, epsilon_slope, and epsilon_root denote uncertainties in sigma(q_inf), sigma'(q_sigma), and q_sigma respectively. To leading order,

|delta Delta q_lin|
approximately
|Delta q_lin| [
  |epsilon_sigma/sigma(q_inf)|
  + |epsilon_slope/sigma'(q_sigma)|
].

The split should not be promoted to a physical result unless

|Delta q_root|

is larger than the combined numerical uncertainty and is stable under domain refinement.

## 5. Interpretation if the relation closes

If

Delta q_root approximately Delta q_lin != 0

with convergence under L, mesh, and derivative step size, then the observed separation cannot be attributed merely to an isolated root-finder artifact: the local slope of the planar tension independently predicts the same displacement.

This would still not by itself establish novelty. It would establish numerical and analytic consistency inside this model.

## 6. Connection to the curvature program

If q_sigma != q_inf, then sigma(q_inf) is nonzero and the decomposition

G_wall(R) = 2 pi R sigma + 2 pi A0 + ...

must retain an explicit radius/dividing-surface convention at q_inf.

At q_sigma, however, the simple translation ambiguity of the first moment is suppressed because sigma=0. Thus q_sigma remains the preferred point for testing the intrinsic constant-curvature sector, while q_inf is the physically relevant point for matching the large-n critical sequence.

This distinction provides a clean two-stage strategy:

1. determine intrinsic curvature structure at q_sigma;
2. transport it to q_inf with the radius/ensemble convention stated explicitly.

## 7. Scientific status

DERIVED:

- the local relation Delta q = -sigma(q_inf)/sigma'(q_sigma) + O(Delta q^2);
- an independent ratio test R_split -> 1;
- the numerical uncertainty conditions required before interpreting a split physically.

NOT YET ESTABLISHED:

- that Delta q is nonzero in the infinite-domain limit;
- that the linear remainder is negligible at current numerical precision;
- novelty relative to prior multicomponent-superconductor literature.

## 8. Impact potential — science and technology

### Science

- **Multicomponent superconductivity:** distinguishes a planar zero-tension criterion from a large-winding critical criterion using an independently testable local relation.
- **Interface thermodynamics:** provides a derivative-based consistency check for small separations between competing definitions of criticality.
- **Topological-defect asymptotics:** the same logic can be applied whenever a planar wall criterion and a curved-defect criterion are close but not obviously identical.
- **Numerical field theory:** gives a robust way to determine whether a tiny critical split is physical or below solver/domain resolution.

### Technology

- **Critical-regime modeling:** if an experimentally relevant multicomponent material exhibits distinct criteria, design models based on a single critical parameter could be refined.
- **Superconducting-device simulation:** more precise identification of flux-nucleation and large-vortex thresholds could improve reduced-order models near crossover regimes.
- **Computation:** the local derivative test can rule in or rule out a split using planar calculations before expensive finite-n scans are performed.

All technological implications remain conditional on cross-parameter validation and later material/experimental calibration.
