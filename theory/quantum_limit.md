# Quantum / Wave Limit

## Status

`known-limit` for the complex-scalar amplitude/phase representation; `candidate` for any claim that the master equation provides a new quantum formulation.

## Complex field and phase

The master variables are organized through

\[
\psi=\sqrt{\rho}\,e^{i\Theta/2}.
\]

This amplitude-phase decomposition is standard. Its value here is that the same variables used for vortices and coupling can be carried into wave and quantum limits without changing representation.

## Relativistic field limit

For a conventional complex scalar action,

\[
\mathcal L=|D_\mu\psi|^2-V(|\psi|^2,\chi)+\frac12(\partial\chi)^2,
\]

variation with respect to \(\psi^*\) gives a nonlinear Klein-Gordon-type equation,

\[
D_\mu D^\mu\psi+\frac{\partial V}{\partial\psi^*}=0.
\]

This is an established field-theory limit and is tagged `known-limit`.

## Phase current

When the potential preserves the relevant global phase symmetry, Noether's theorem yields a conserved current. In amplitude-phase variables this current is proportional to the density multiplied by the phase gradient, with the gauge-covariant form used when \(A_\mu\neq0\).

The corresponding conservation law is

\[
\partial_\mu J^\mu=0.
\]

## Nonrelativistic target

A controlled nonrelativistic reduction should be derived rather than assumed. The target is a Schrödinger/Gross-Pitaevskii-type effective equation under the appropriate separation of the rapid rest-energy phase and slow envelope.

This reduction should establish precisely which parameters in the master action map to effective mass, nonlinear coupling and external/effective potentials.

## Mixed modes

Around a stable homogeneous vacuum, fluctuations in the scalar amplitudes can mix. The Hessian of the potential determines the normal-mode mass matrix,

\[
M^2_{ij}=\left.\frac{\partial^2V}{\partial\phi_i\partial\phi_j}\right|_{\rm vac},
\]

whose eigenvalues define the mixed masses \(m_+^2\) and \(m_-^2\). Their inverse scales determine characteristic coherence lengths when the corresponding modes are stable.

## What is not yet established

The repository does not yet claim that:

- the master equation replaces quantum mechanics;
- the 4\pi phase structure is required by observed quantum physics;
- quantum measurement emerges from \(\rho,\Theta,\chi\);
- the coupled fields produce new quantum predictions.

Those remain separate hypotheses and require explicit derivation and tests.

## Numerical validation targets

1. Recover linear dispersion in the weak-field limit.
2. Verify Noether-current conservation.
3. Derive and test the nonrelativistic envelope limit.
4. Compare mixed-mode spectra against direct Hessian eigenvalues.
5. Test vortex phase winding and stability without imposing desired outcomes.
