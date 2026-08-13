# V0.1 Scientific Validation Report

## 1. Executive summary

The full campaign was attempted but could not start because the required numerical packages are unavailable and downloads are blocked (HTTP 403). No scientific value was fabricated or inferred from an unexecuted calculation. Overall status: **INCOMPLETE**.

## 2. PASS / FAIL / INCOMPLETE table

| Block | Status | Evidence |
|---|---|---|
| A | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |
| B | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |
| C | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |
| D | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |
| E | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |
| F | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |
| G | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |
| H | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |
| I | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |
| J | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |
| K | **INCOMPLETE** | Campaign could not import required numerical dependencies; no result inferred. |

## 3. Exact reproduction commands

```bash
python -m pip install -r requirements-validation.txt
python -m validation.run_v01 --quick
python -m validation.run_v01 --full
```

## 4. Environment

Exact local details and the dependency limitation are in `environment.json`.

## 5. Convergence evidence

No numerical solve ran locally. CSV schemas are present, but contain no records. The full command populates all convergence metadata.

## 6. Numerical uncertainties

No uncertainties are reported for unexecuted calculations. The runner records BVP residual estimates and root-bracket uncertainties separately.

## 7. Failed/nonconvergent cases

The environmental failure is preserved in `failures.json`. When dependencies are available, solver failures are retained per case and do not abort subsequent blocks.

## 8. Known physics reproduced

Not locally executed. Blocks A and B are designed to test the mixed-vacuum identities, scalar masses, the c=0 reduction, and the known Abelian-Higgs Bogomolny benchmark without novelty claims.

## 9. Model-specific results

None are claimed from this blocked execution.

## 10. Candidate novel contributions requiring literature verification

Controlled small-c displacement, reduction to `C(rho_X)`, and quantitative interface-to-high-winding matching remain candidates pending successful computation, rigorous derivation, and literature verification.

## 11. Explicit blockers for v0.1.0

The campaign must be rerun in an environment providing the pinned dependencies. Independently, the complete bulk-subtracted quadratic Gibbs functional and interface curvature conversion required by blocks G, H, and J must be rigorously derived; the runner deliberately marks these items INCOMPLETE rather than inventing a formula.
