# coupled-field-vortex-model

Reproducible research project for a coupled Abelian-Higgs field and real neutral scalar, focused on vortex criticality, planar-interface energy, perturbations of the Bogomolny boundary, and numerical validation.

The project is formulated entirely in the standard language of classical field theory, Abelian gauge theory, Ginzburg–Landau theory, topological defects, and superconductivity. It is scientifically distinct from Resolutive Physics.

## Archival record

- V0.1.0 DOI: `10.5281/zenodo.21936796`
- Concept DOI (all versions): `10.5281/zenodo.21936795`
- Archived version: `v0.1.0`

For reproducibility of the V0.1 scientific results, cite the version-specific DOI above. The concept DOI should be used when referring to the software project across versions.

## Reference model

The dimensionless scalar sector is

\[
\widehat{\mathcal L}
=
|D\psi|^2
+\frac12(\partial X)^2
-\widehat V(\psi,X)
-\frac14F_{\mu\nu}F^{\mu\nu},
\]

with

\[
D_\mu=\partial_\mu-iqA_\mu,
\]

and

\[
\widehat V
=
a|\psi|^2+b|\psi|^4+c|\psi|^2X^2
-\frac12X^2+\frac14X^4.
\]

## V0.1 central result

Around the decoupled Bogomolny point

\[
q_{\rm BPS}^2=2b,
\]

the critical boundary is obtained perturbatively as

\[
q_{\rm crit}^2
=
2b-C(\rho_X)c^2+O(c^3),
\]

where

\[
C(\rho_X)
=
\frac{
\int_{-\infty}^{+\infty}F^2(x)[1+U_{\rho_X}(x)]\,dx
}{
\int_{-\infty}^{+\infty}G^2(x)F^2(x)\,dx
},
\]

and

\[
U_{\rho_X}''
=
\frac{U_{\rho_X}+F^2}{\rho_X}.
\]

Within the V0.1 derivation:

- the complete planar Gibbs contribution at \(O(c)\) cancels on the BPS background;
- the charged first-order response sector cancels on shell at \(O(c^2)\);
- the critical displacement is controlled by the neutral response;
- the universal coefficient agrees with independent full interface roots;
- the resolved truncation residual scales consistently with \(O(c^3)\).

## Validation status

The frozen H–J scientific acceptance criteria are documented in:

- `docs/V01_HIJ_ACCEPTANCE.md`
- `validation/hij_checks.py`

Within the agreed V0.1 scope, blocks A–F and H–K pass the scientific gate. Block G — complete quantitative interface-to-giant-vortex curvature matching — remains complementary and is deferred beyond the central V0.1 claim.

## Scientific positioning

The model class, Bogomolny framework, near-critical perturbation techniques, and giant-vortex methods have prior literature. They are not claimed as new.

The V0.1 candidate contribution is the specific neutral-scalar-induced displacement law above, its analytic cancellation structure, and its numerical validation. Novelty language should remain conservative until the final literature audit is complete.

## Reproducibility

Run the validation campaign with

```bash
python -m validation.run_v01 --quick
python -m validation.run_v01 --full
```

The archived V0.1.0 release preserves machine-readable outputs, environment metadata, solver tolerances, convergence diagnostics, and the frozen acceptance criteria.

## Licensing

This project uses a source-available academic-use license:

- accredited universities and public research institutes: academic research/teaching use without license fee under `LICENSE.md`;
- commercial products, paid services, proprietary integrations, commercial deliverables, or monetized redistribution: separate written commercial license required.

This is not an OSI-approved open-source license. No patent rights are granted except by separate written agreement. See `LICENSE.md` and `COMMERCIAL_LICENSE.md` for the controlling terms.

## Release

Current archived research release: `v0.1.0`.

Version-specific DOI: `10.5281/zenodo.21936796`.
