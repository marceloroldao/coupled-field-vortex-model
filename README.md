# coupled-field-vortex-model

Research project for a coupled complex scalar, real scalar, and Abelian gauge-field model, focused on mixed scalar modes, vortex interactions, interfacial energy, criticality, and reproducible numerical tests.

The project is formulated entirely in the standard language of classical field theory, Abelian gauge theory, Ginzburg–Landau theory, topological defects, and superconductivity. Its scientific claims are evaluated directly against the established literature in those areas.

## Current model

The minimal dimensionless scalar sector is

\[
\widehat{\mathcal L}=|\partial\psi|^2+\frac12(\partial X)^2-\widehat V(\psi,X),
\]

with

\[
\widehat V=a|\psi|^2+b|\psi|^4+c|\psi|^2X^2-\frac12X^2+\frac14X^4.
\]

The Abelian gauge extension is obtained through

\[
D_\mu=\partial_\mu-iqA_\mu,
\qquad
-\frac14F_{\mu\nu}F^{\mu\nu}.
\]

Classical scalar dynamics are controlled primarily by `(a, b, c)`, with `q` entering the gauge sector.

## Research goals

- derive and verify the phase diagram of the coupled-field model;
- compute the mixed scalar normal modes `m_+` and `m_-` and the associated correlation/coherence lengths;
- map vortex interaction regimes, including separated vortices, bound states, and multiquanta vortices;
- determine the relation between planar interfacial tension and the stability of high-winding vortices;
- test spectral and nonlinear classifiers for vortex behavior;
- quantify non-pairwise interactions for three or more vortices;
- compare directly with multicomponent Ginzburg–Landau, Abelian-Higgs, type-I/type-II, and type-1.5 literature;
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

- `theory/` — action, Euler–Lagrange equations, vacuum structure, phase diagram, normal modes, and analytic limits;
- `src/` — reusable model and solver implementation;
- `simulations/` — reproducible numerical experiment entry points;
- `tests/` — unit, regression, convergence, and physics-consistency tests;
- `benchmarks/` — parameter sweeps and comparison baselines;
- `results/` — machine-readable outputs and summarized findings;
- `docs/` — methodology, numerical conventions, decisions, and validation reports;
- `paper/` — manuscript sources and figures;
- `references/` — literature notes and comparison matrix.

## Methodological rule

New interaction terms, interpretations, or parameter choices are not added to the reference action merely because they produce a desired solution. A proposed extension must be compared with the minimal model, subjected to analytical and numerical consistency tests, and retained only when independently justified by symmetry, effective-field-theory reasoning, microscopic derivation, or empirical evidence.

## Current status

Active numerical-validation phase. The working reference is the minimal coupled scalar–Abelian-gauge model above. Numerical claims must be reproducible from repository code, include convergence checks where applicable, and be distinguished from analytic results and literature-known limits.
