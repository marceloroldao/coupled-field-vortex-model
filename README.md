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

## Research goals

- derive and verify the phase diagram of the coupled-field model;
- compute the mixed scalar modes `m_+` and `m_-` and their coherence lengths;
- map vortex interaction regimes: separated, molecular and fused;
- test spectral/nonlinear classifiers for vortex behavior;
- quantify non-pairwise interactions for three or more vortices;
- compare against multicomponent Ginzburg–Landau, Abelian-Higgs and type-1.5 literature;
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

Bootstrap phase. The working reference is the minimal coupled-field model above. Results discussed during exploration must be re-run from repository code before being marked `numerical` or used in publication.
