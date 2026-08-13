# Cosmological Homogeneous-Field Limit

## Status

`candidate` reduction of the coupled-field model on a homogeneous and isotropic background. Standard scalar-field cosmology recovered from the same action is a `known-limit`; any phenomenological improvement is not yet established.

## FLRW background

Take the spatially flat FLRW metric

\[
ds^2=-dt^2+a(t)^2d\mathbf{x}^2,
\qquad H=\frac{\dot a}{a}.
\]

For homogeneous scalar configurations, spatial gradients are neglected and the master fields reduce to time-dependent variables,

\[
\rho=\rho(t),\qquad \Theta=\Theta(t),\qquad \chi=\chi(t).
\]

## Effective energy density and pressure

For the scalar master sector,

\[
\mathcal L_{\rm M}=\frac{1}{4\rho}(\partial\rho)^2+\frac{\rho}{4}(\partial\Theta)^2+\frac12(\partial\chi)^2-V(\rho,\chi),
\]

the homogeneous kinetic contribution can be collected as

\[
K=\frac{\dot\rho^2}{4\rho}+\frac{\rho\dot\Theta^2}{4}+\frac{\dot\chi^2}{2},
\]

up to the chosen metric-sign convention. The associated effective scalar energy density and pressure take the standard form

\[
\rho_{\rm eff}=K+V,
\qquad
p_{\rm eff}=K-V.
\]

Hence

\[
w_{\rm eff}=\frac{p_{\rm eff}}{\rho_{\rm eff}}.
\]

## Friedmann coupling

When coupled minimally to general relativity, the background dynamics satisfy the standard Friedmann equations,

\[
H^2=\frac{8\pi G}{3}\rho_{\rm total},
\]

and

\[
\frac{\ddot a}{a}=-\frac{4\pi G}{3}(\rho_{\rm total}+3p_{\rm total}).
\]

The master fields contribute through \(\rho_{\rm eff}\) and \(p_{\rm eff}\).

## Phase dynamics

If the potential is independent of \(\Theta\), the homogeneous phase equation gives a conserved comoving charge of the form

\[
a^3\rho\dot\Theta=\text{constant},
\]

up to normalization. This provides a direct bridge between phase dynamics, dilution by expansion and effective equation-of-state behavior.

## Criticality and transitions

Because the potential couples the complex-scalar density to the real scalar, for example through a term such as

\[
c\rho\chi^2,
\]

the effective curvature of the \(\chi\) potential depends on \(\rho\). This can generate density-dependent changes in vacuum stability or phase transitions. The exact critical density must be derived from the chosen normalized potential, not imported from a different parametrization.

## What is established

Scalar-field dynamics on FLRW backgrounds and their contribution to effective density and pressure are standard cosmological field theory and therefore `known-limit`.

## What must be tested

The independent model becomes scientifically interesting only if the coupled \((\rho,\Theta,\chi)\) geometry yields a constrained cosmological consequence not inserted by hand, for example:

- a calculable transition scale;
- a restricted equation-of-state trajectory;
- a characteristic perturbation spectrum;
- a relation between microscopic mixed modes and cosmological evolution;
- a quantitative observable differing from a standard scalar-field baseline.

## Numerical validation targets

1. Integrate the homogeneous field equations together with Friedmann evolution.
2. Check covariant energy conservation.
3. Map stable and unstable homogeneous fixed points.
4. Derive the effective \(w(a)\) rather than fitting it as an independent ansatz.
5. Compare the background expansion against standard scalar-field cosmology before claiming novelty.
