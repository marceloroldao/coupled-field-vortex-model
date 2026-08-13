# Master Equation Reference

## Status

`candidate` reference formulation for the coupled-field-vortex model.

This document records the current compact variational core used to organize the model. It is intentionally separated from Resolutive Physics and should be evaluated as an independent field-theory construction.

## Fields

We use a complex scalar field written in amplitude-phase variables,

\[
\psi=\sqrt{\rho}\,e^{i\Theta/2},
\qquad \rho\ge 0,
\]

plus a real scalar coherence/coupling field \(\chi\). When the gauge sector is active, the phase is minimally coupled through \(A_\mu\).

## Minimal scalar action

A compact scalar-sector Lagrangian is

\[
\mathcal L_{\rm M}=
\frac{1}{4\rho}(\partial_\mu\rho)(\partial^\mu\rho)
+\frac{\rho}{4}(\partial_\mu\Theta)(\partial^\mu\Theta)
+\frac12(\partial_\mu\chi)(\partial^\mu\chi)
-V(\rho,\chi).
\]

This form is equivalent to the kinetic term of a complex scalar written in polar variables, supplemented by a real scalar field.

## Gauge extension

For the electromagnetic sector,

\[
D_\mu=\partial_\mu-iqA_\mu,
\qquad
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu,
\]

and the gauge-field term is

\[
-\frac14F_{\mu\nu}F^{\mu\nu}.
\]

The phase-gradient contribution is then replaced by the corresponding gauge-covariant expression.

## Example potential

The dimensionless reference potential currently used in the repository is

\[
\widehat V=a|\psi|^2+b|\psi|^4+c|\psi|^2X^2-\frac12X^2+\frac14X^4.
\]

In amplitude notation, \(|\psi|^2=\rho\).

## Interpretation rule

The master-equation program is not to rename established equations. The test is whether multiple effective regimes can be derived from the same action with fewer independent assumptions.

Candidate regimes to test are:

1. gauge/electromagnetic limit;
2. quantum/wave limit;
3. cosmological homogeneous-field limit;
4. vortex and mixed-mode regimes;
5. classical effective limits where appropriate.

Each claimed reduction must be labeled `known-limit`, `derived`, `numerical`, `candidate`, or `rejected` according to the repository convention.

## Important exclusions

The golden ratio is not part of the current master equation. Any anti-resonance or golden-ratio sector must remain separate unless independently derived from the stated action and stability conditions.

## Validation target

The strongest form of the program would be

\[
\mathcal L_{\rm M}
\longrightarrow
\{\text{multiple established effective limits}\}
\]

without introducing a new phenomenological rule for every regime. Until that is demonstrated, the master equation must be treated as a compact organizing framework rather than a unified theory of physics.
