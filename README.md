# coupled-field-vortex-model

Independent research project for a coupled complex-scalar, real-scalar and gauge-field model focused on mixed modes, vortex interactions, criticality and reproducible numerical tests.

> **Scientific separation:** this repository is **not** part of Resolutive Physics / `resolutive-science`. It follows the same engineering, reproducibility and documentation standards, but represents an independent field-theory research line.

## Current model

The minimal dimensionless scalar sector is

\[
\widehat{\mathcal L}=|\partial\psi|^2+\frac12(\partial X)^2-\widehat V(\psi,X),
\]

with

\[
\widehat V=a|\psi|^2+b|\psi|^4+c|\psi|^2X^2-\frac12X^2+\frac14X^4.
\]

The electromagnetic extension is obtained through

\[
D_\mu=\partial_\mu-iqA_\mu,
\qquad
-\frac14F_{\mu\nu}F^{\mu\nu}.
\]

Classical scalar dynamics are controlled primarily by `(a, b, c)`, with `q` entering the gauge sector.

## Master-equation program

The current compact variational reference and its principal effective-limit targets are documented in:

- [`theory/master_equation.md`](theory/master_equation.md) — master-equation reference, variables, scope and validation rule;
- [`theory/electromagnetic_limit.md`](theory/electromagnetic_limit.md) — Abelian gauge / Maxwell limit and validation targets;
- [`theory/quantum_limit.md`](theory/quantum_limit.md) — complex-scalar, phase-current, mixed-mode and nonrelativistic quantum/wave limits;
- [`theory/cosmological_limit.md`](theory/cosmological_limit.md) — homogeneous FLRW reduction, effective density/pressure and cosmological validation targets.

These files distinguish established physics (`known-limit`) from model-specific hypotheses (`candidate`). Recovery of a known equation is not treated as novelty by itself.

## Research goals

- derive and verify the phase diagram of the coupled-field model;
- compute the mixed scalar modes `m_+` and `m_-` and their coherence lengths;
- map vortex interaction regimes: separated, molecular and fused;
- test spectral/nonlinear classifiers for vortex behavior;
- quantify non-pairwise interactions for three or more vortices;
- compare against multicomponent Ginzburg–Landau, Abelian-Higgs and type-1.5 literature;
- derive and verify electromagnetic, quantum/wave and cosmological effective limits from the same variational core;
- document negative results and rejected hypotheses;
- maintain fully reproducible numerical experiments.

## Result-status convention

Every scientific claim should be tagged with one of:

- `derived` — follows analytically from the stated action and assumptions;
- `numerical` — reproduced by a documented numerical experiment;
- `candidate` — plausible result awaiting stronger validation;
- `rejected` — tested and not supported;
- `known-limit` — recovery of established physics, not claimed as novelty.

## Planned structure

- `theory/` — action, derivations, phase diagram and analytic limits;
- `src/` — reusable model and solver implementation;
- `simulations/` — reproducible experiment entry points;
- `tests/` — unit, regression and physics-consistency tests;
- `benchmarks/` — parameter sweeps and comparison baselines;
- `results/` — machine-readable outputs and summarized findings;
- `docs/` — methodology, decisions and validation reports;
- `paper/` — manuscript sources and figures;
- `references/` — literature notes and comparison matrix.

## Methodological rule

New terms, interpretations or parameter choices are not promoted into the reference model merely because they produce a desired solution. A proposal must be tested against the previous version, documented, and retained only if it improves consistency, predictive value or empirical performance.

## Current status

Bootstrap phase. The working reference is the minimal coupled-field model above. The master-equation and effective-limit documents define the current derivation targets. Results discussed during exploration must be re-run from repository code before being marked `numerical` or used in publication.
