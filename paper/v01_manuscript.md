# Neutral-scalar-induced displacement of the Bogomolny boundary in a coupled Abelian-Higgs model

**Marcelo Roldão Matos**

## Abstract

We study a coupled Abelian-Higgs model containing a charged complex scalar and an additional real neutral scalar with quartic cross-coupling. The model class itself is established; our focus is the perturbative displacement of the critical Bogomolny boundary induced by the neutral-scalar interaction. Expanding around the decoupled Bogomolny point \(q^2=2b\), we show that the complete planar Gibbs contribution linear in the inter-field coupling \(c\) cancels on the BPS background. At second order, the charged first-order response sector reduces on shell to vanishing BPS-linearized combinations, leaving only the neutral response. The critical boundary therefore takes the form

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

Numerical boundary-value calculations independently reproduce the coefficient at representative mass ratios, while the residual between the full interface calculation and the second-order formula is consistent with cubic scaling in the resolved perturbative regime. The result provides a compact response formula for how a neutral scalar shifts the type-I/type-II critical boundary in this coupled-field setting.

## 1. Scope and prior art

The Abelian-Higgs model, its Bogomolny point, near-critical perturbation theory, neutral-scalar extensions, and large-winding vortex asymptotics have substantial prior literature. This work does not claim novelty for those frameworks. The candidate contribution is the specific critical-boundary displacement derived below, including the first-order cancellation, charged-sector second-order cancellation, universal neutral-response coefficient, and direct numerical validation.

## 2. Model

Use the dimensionless action documented in `theory/MODEL.md`, with

\[
V=a|\psi|^2+b|\psi|^4+c|\psi|^2X^2-\frac12X^2+\frac14X^4.
\]

The gauge covariant derivative is \(D_\mu=\partial_\mu-iqA_\mu\).

## 3. Decoupled Bogomolny reference point

At \(c=0\),

\[
q_{\rm BPS}^2=2b.
\]

Introduce universal planar BPS profiles \(F,G\), satisfying

\[
F'=-GF,\qquad G'=1-F^2.
\]

## 4. First-order cancellation

Expand the bulk condensate, critical field, fields, and planar Gibbs density in \(c\). The explicit cross-coupling contribution, the variation of the Gibbs magnetic term, and the superconducting bulk subtraction cancel pointwise at \(O(c)\). Hence

\[
\left.\frac{\partial \sigma}{\partial c}\right|_{c=0}=0,
\]

so the critical displacement begins at \(O(c^2)\).

## 5. Charged response at second order

The charged first-order responses \(P,R\) satisfy the linearized BPS identities

\[
P'+GP+FR=0,
\]

\[
R'+2FP+1=0.
\]

The charged quadratic Gibbs contribution can be organized as

\[
Q_{\rm ch}
=
\int\left[
\frac12(P'+GP+FR)^2
+
\frac14(R'+2FP+1)^2
\right]dx
\]

plus vanishing boundary terms. Therefore

\[
Q_{\rm ch}=0
\]

on shell.

## 6. Neutral response and universal coefficient

The neutral response satisfies

\[
U_{\rho_X}''
=
\frac{U_{\rho_X}+F^2}{\rho_X},
\]

with asymptotic conditions \(U(-\infty)=0\), \(U(+\infty)=-1\).

The surviving second-order numerator reduces to

\[
I_X(\rho_X)=\int F^2(1+U_{\rho_X})\,dx,
\]

while the critical sensitivity to \(q^2\) is

\[
I_D=\int G^2F^2\,dx.
\]

Thus

\[
C(\rho_X)=\frac{I_X}{I_D},
\]

and

\[
q_{\rm crit}^2
=
2b-C(\rho_X)c^2+O(c^3).
\]

## 7. Numerical validation

Representative universal values are approximately

- \(C(0.30)\approx2.29083\),
- \(C(0.40)\approx2.37498\),
- \(C(0.50)\approx2.45488\).

They agree with independently extracted full-interface roots within the pre-declared V0.1 tolerance. The charged diagnostic is numerically close to zero, and the universal solutions satisfy the linearized BPS identities well below the frozen residual thresholds.

At the resolved reference point, the truncation residual

\[
R(c)=q_{\rm crit,full}^2-[2b-Cc^2]
\]

scales approximately as \(c^3\).

## 8. Giant-vortex connection

Large-winding and planar-interface calculations are included as complementary validation. A fully controlled conversion from planar interface tension to the finite-curvature coefficient of the giant-vortex expansion is not required for the central V0.1 result and remains deferred.

## 9. Limitations

The result is perturbative in \(c\). The present work does not establish a material-specific prediction, experimental realization, or industrial design rule. It also does not claim that the underlying model class is new. A final literature audit should precede any priority statement stronger than “candidate contribution.”

## 10. Reproducibility

The archived release should contain solver code, frozen thresholds, convergence diagnostics, machine-readable outputs, environment metadata, and the exact release commit.

## 11. Conclusion

A neutral scalar coupled to the charged condensate shifts the Bogomolny critical boundary only at second order in the cross-coupling within the perturbative regime considered. The charged response cancels on shell, and the remaining shift is governed by a single universal neutral-response integral.
