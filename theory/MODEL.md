# Reference Model

## Status

`derived` for the variational equations and algebraic phase conditions once independently reproduced from this file.

## Dimensionless scalar action

\[
S=\int d^4x\left[|\partial\psi|^2+\frac12(\partial X)^2-V(\psi,X)\right],
\]

with

\[
V=a|\psi|^2+b|\psi|^4+c|\psi|^2X^2-\frac12X^2+\frac14X^4.
\]

The scalar sector is invariant under `U(1)_psi x Z2_X`.

## Gauge extension

\[
D_\mu=\partial_\mu-iqA_\mu,
\qquad
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu,
\]

with

\[
\mathcal L_{EM}=-\frac14F_{\mu\nu}F^{\mu\nu}+|D\psi|^2+\frac12(\partial X)^2-V.
\]

## Mixed phase

For a mixed homogeneous vacuum,

\[
|\psi_0|^2=-\frac{a+c}{2(b-c^2)},
\qquad
X_0^2=\frac{b+ac}{b-c^2}.
\]

A conventional stable mixed branch requires

\[
b-c^2>0,\quad a+c<0,\quad b+ac>0.
\]

## Mixed scalar modes

Writing the radial fluctuation of the complex field as `h` and the real-scalar fluctuation as `x`, the mass matrix is

\[
M_s^2=2\begin{pmatrix}
bv^2 & cvX_0\\
cvX_0 & X_0^2
\end{pmatrix},
\]

where `v^2=2|psi_0|^2`. Its eigenvalues define

\[
m_-^2\le m_+^2.
\]

The associated coherence lengths are

\[
\xi_-=m_-^{-1},\qquad \xi_+=m_+^{-1}.
\]

The gauge-field mass in the condensed phase is

\[
m_A=qv,\qquad \lambda_L=m_A^{-1}.
\]

## Current research hypotheses

These are **not** yet reference results:

- a finite molecular-vortex window can occur when long-range scalar attraction coexists with a positive fusion cost;
- a compact classifier may predict `Delta_2 = E_(n=2)-2E_(n=1)` from spectral and nonlinear vacuum data;
- near criticality, the light mixed mode may produce long-range effective behavior relevant to extended field configurations.

Each hypothesis must be reproduced numerically from repository code before promotion.
