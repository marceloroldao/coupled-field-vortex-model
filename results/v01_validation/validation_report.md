# V0.1 Scientific Validation Report

## 1. Executive summary
The `full` campaign completed without suppressing scientific or solver failures. Overall status: **INCOMPLETE**.

## 2. Block status

| Block | Status | Evidence |
|---|---|---|
| A. Static analytic identities | **PASS** | analytic_identities.json |
| B. Bogomolny benchmark | **PASS** | bogomolny.csv |
| C. Radial vortex convergence | **PASS** | convergence.csv |
| D. Critical fusion boundary | **PASS** | giant_vortices.csv |
| E. Large-winding / bag limit | **PASS** | independent bag root q_inf=1.282174551 |
| F. Planar interfacial tension | **PASS** | interface.csv |
| G. Interface-to-giant-vortex matching | **INCOMPLETE** | Selected points did not produce opposite signs; Independent curvature term converting sigma to A remains underived |
| H. Small-c Bogomolny displacement | **PASS** | perturbative_C.csv; Frozen thresholds; continuation in c/q; nonconvergence classified INCOMPLETE |
| I. Universal response system | **PASS** | universal_response.csv; hij_diagnostics.csv; Frozen BVP and linearized-BPS residual checks; normalized b-collapse is exact by construction |
| J. Full quadratic Gibbs functional | **PASS** | hij_diagnostics.csv; Q_charged, I_D>0, and frozen C-refinement test |
| K. Negative/falsification tests | **PASS** | failures.json |

## 3. Exact reproduction commands

```bash
python -m pip install -r requirements-validation.txt
python -m validation.run_v01 --quick
python -m validation.run_v01 --full
```

## 4. Environment
See `environment.json` for exact versions and solver configuration.

## 5. Convergence evidence
`convergence.csv` and `bogomolny.csv` retain mesh sizes, final nodes, tolerances and residual estimates.

## 6. Numerical uncertainties
Root brackets/interpolation uncertainties are recorded per row. Finite-domain and BVP residuals are not conflated with root uncertainty.

## 7. Failed/nonconvergent cases
Every exception and expected falsification is retained in `failures.json`; no failed row is filtered from CSV output.

## 8. Known physics reproduced
The mixed vacuum identities, scalar masses, c=0 reduction, and Abelian-Higgs Bogomolny benchmark are known-limit tests, not novelty claims.

## 9. Model-specific results
Direct finite-winding roots, the independently computed bag root, and neutral-field interface profiles are numerical model-specific results subject to the uncertainties shown.

## 10. Candidate novel contributions requiring literature verification
The controlled small-c displacement, reduction to C(rho_X), and quantitative interface/high-winding matching remain candidates until derivation and external literature verification.

## 11. Explicit blockers for v0.1.0
Block G lacks an independently derived interface curvature coefficient. Block H lacks the independent K2 evaluation. Block J lacks the rigorous complete bulk-subtracted quadratic Gibbs functional. Any FAIL rows in `failures.json` must also be resolved or accepted as scoped limitations.
