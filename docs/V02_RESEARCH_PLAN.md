# V0.2 Research Plan — Curvature Closure

## Status

This document freezes the first scientific target and acceptance logic for V0.2 before new V0.2 numerical results are used to tune the criteria.

V0.1.0 remains the immutable reproducible baseline. V0.2 must not rewrite a negative or incomplete V0.1 result as a success.

## Primary scientific question

V0.1 established a reproducible planar-interface calculation and a large-winding numerical sector, but the independent curvature term needed to convert planar interface tension into the subleading large-winding vortex correction remained underived.

V0.2 asks whether that missing bridge can be derived and then tested out of sample.

The working asymptotic organization is

E_n = E_bulk(n) + E_interface(n) + E_curv(n) + ...

with a large vortex radius R_n and

E_interface = 2 pi R_n sigma.

The curvature sector must be obtained from the field functional and geometry, not introduced merely as a fit coefficient to the radial-vortex data.

## G1 — Analytic decomposition

Derive the large-R expansion directly from the model functional in local coordinates normal/tangent to the interface.

Required separation:

1. bulk contribution;
2. planar interface contribution proportional to sigma;
3. first curvature correction;
4. remainder with an explicit asymptotic order.

PASS: the coefficient and sign convention of the curvature contribution are defined by an explicit integral/functional of independently computed profiles.

FAIL: the required coefficient is inferred only by fitting giant-vortex energies or critical couplings.

INCOMPLETE: the expansion can be organized but a boundary, ensemble, gauge, or matching term remains unresolved.

## G2 — Independent curvature observable

Implement a numerical evaluator for the G1 curvature functional using planar-interface / linear-response data only.

The evaluator must record convergence under at least:

- domain enlargement;
- mesh refinement;
- solver tolerance refinement.

PASS: the curvature observable converges to a stable finite value under frozen tolerances.

FAIL: it diverges, changes sign without convergence, or depends materially on arbitrary numerical choices.

INCOMPLETE: solver nonconvergence prevents classification.

## G3 — Parameter-free prediction

Use the independently evaluated interface and curvature quantities to predict a large-winding observable before comparing with the radial solver.

No coefficient may be calibrated on the held-out radial points used for validation.

The prediction table must contain predicted value, radial-solver value, absolute error, relative error, winding n, and numerical uncertainty where available.

## G4 — Out-of-sample radial test

Split winding numbers into derivation/development and held-out validation sets before final evaluation.

The held-out set is the scientific gate.

PASS: residuals decrease consistently with the asymptotic order derived in G1 and the held-out prediction agrees within the combined frozen numerical/asymptotic error budget.

FAIL: the residual scaling contradicts the derived order or the held-out points systematically miss the frozen error budget.

INCOMPLETE: insufficient converged held-out radial solutions.

## G5 — Robustness

Repeat the closure test for more than one admissible parameter point around the V0.1 reference regime. A single-point numerical coincidence is not sufficient for a general V0.2 claim.

PASS: the same derived functional and conventions work without refitting its form.

FAIL: the closure requires point-by-point empirical coefficients.

## Baseline regression gate

Every V0.2 commit must continue to run:

- unit tests;
- V0.1 quick validation;
- V0.1 full validation.

A V0.2 result cannot be accepted if it silently breaks a V0.1 PASS block.

## Evidence layout

New V0.2 evidence should be written under `results/v02_validation/` and should not overwrite the archived V0.1 evidence.

Planned machine-readable evidence:

- `curvature_functional.csv`
- `curvature_convergence.csv`
- `large_n_predictions.csv`
- `heldout_residuals.csv`
- `v02_summary.json`
- `v02_validation_report.md`

## Scientific reporting rule

PASS, FAIL, and INCOMPLETE are all valid scientific outcomes. Numerical thresholds must be frozen in code/documentation before the final held-out run. No threshold may be relaxed because of the observed held-out result. No missing analytic term may be replaced by an invented formula.
