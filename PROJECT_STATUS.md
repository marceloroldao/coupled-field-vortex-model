# Project Status

## Scientific identity

Independent coupled-field research line formulated in standard classical field theory and superconductivity language. This project is intentionally distinct from Resolutive Physics.

## Release target

`v0.1.0` — first reproducible research release and Zenodo archival target.

## Central V0.1 result

\[
q_{\rm crit}^2
=
2b-C(\rho_X)c^2+O(c^3),
\]

with

\[
C(\rho_X)=
\frac{\int F^2(1+U_{\rho_X})\,dx}
{\int G^2F^2\,dx},
\qquad
U_{\rho_X}''
=
\frac{U_{\rho_X}+F^2}{\rho_X}.
\]

The derivation includes exact \(O(c)\) Gibbs/bulk cancellation, on-shell charged-sector cancellation at \(O(c^2)\), reduction to the neutral response, full-interface numerical checks, and \(O(c^3)\) truncation scaling.

## Gate status

- A: PASS
- B: PASS
- C: PASS
- D: PASS
- E: PASS
- F: PASS
- G: INCOMPLETE — complementary curvature matching, deferred beyond core V0.1
- H: PASS
- I: PASS
- J: PASS
- K: PASS

No remaining scientific blocker exists for the agreed central V0.1 claim.

## Candidate contribution

The specific neutral-scalar-induced displacement law and universal coefficient are treated as candidate contributions. The underlying Abelian-Higgs + neutral-scalar model class and BPS/giant-vortex frameworks are known.

## Deferred work

- complete interface-to-giant-vortex curvature matching;
- broader high-winding asymptotics;
- multivortex/non-pairwise interactions;
- material-specific or experimental calibration.

## Release engineering

Before Zenodo:

1. synchronize README, manuscript, citation and license metadata;
2. merge the licensing/Zenodo PR;
3. run final repository-level validation on the release commit;
4. create tag/release `v0.1.0`;
5. verify custom academic/commercial licensing in Zenodo;
6. archive the release;
7. record DOI in README/CITATION metadata.
