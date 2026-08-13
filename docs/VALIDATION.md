# Validation Protocol

## V0.1 campaign entry point

The publication-oriented Issue #4 campaign is implemented as one fail-soft
entry point. It writes machine-readable records first and produces figures only
by rereading those records:

```bash
python -m pip install -r requirements-validation.txt
python -m validation.run_v01 --quick
python -m validation.run_v01 --full
```

Outputs are written to `results/v01_validation/`. A scientific disagreement or
individual BVP failure is recorded and does not stop later validation blocks.
The checked-in report describes the most recent execution environment; it must
not be interpreted as a successful campaign when its status is `INCOMPLETE`.

This project uses a strict separation between analytic derivation, numerical evidence, candidate interpretation and rejected hypotheses.

## Required checks

1. **Analytic consistency**
   - dimensions/normalization;
   - symmetry checks;
   - boundedness of the potential;
   - stationary-point Hessian;
   - limiting cases.

2. **Numerical reproducibility**
   - fixed parameter files;
   - fixed random seeds when applicable;
   - grid/box convergence;
   - residual norms;
   - conservation or constraint checks;
   - machine-readable outputs.

3. **Vortex tests**
   - single-vortex convergence;
   - flux quantization;
   - `E_n/n` versus winding `n`;
   - two-vortex interaction energy `E_2v(d)`;
   - comparison of separated, molecular and fused states;
   - non-pairwise corrections for `N >= 3`.

4. **Novelty control**
   - compare with multicomponent Ginzburg-Landau, Abelian-Higgs and type-1.5 literature;
   - do not label a known limit or known phenomenon as novel;
   - novelty claims require a precise difference in equation, regime, relation or observable.

## Result labels

- `derived`
- `numerical`
- `candidate`
- `rejected`
- `known-limit`

## Change-control rule

A new term or interpretation must be tested against the current reference model. Keep both versions and a short replacement report whenever the reference model changes.
