# Bogomolny-limit benchmark

Status: **derived + numerical benchmark / locally reproduced**.

Purpose: verify that the coupled complex-scalar/real-scalar/Abelian-gauge model reduces to the ordinary one-component Abelian-Higgs / Ginzburg–Landau critical point when the biquadratic coupling `c -> 0`.

For `c=0`, the neutral scalar decouples from the charged sector. In the project normalization, the charged free-energy density can be written as

`|D psi|^2 + 1/2 B^2 + b(|psi|^2-v^2)^2`

(up to an irrelevant constant), with `v^2=-a/(2b)`.

Completing squares gives the standard Bogomolny condition

`q_BPS^2 = 2 b`.

At this point the planar normal/superconducting interfacial tension vanishes and multivortex states are degenerate in the ordinary Abelian-Higgs model.

## Numerical recovery

| (a,b,c) | q_BPS=sqrt(2b) | q_inf from radial/large-n crossing | sigma(q_BPS) |
|---|---:|---:|---:|
| (-0.6,1.0,0) | 1.41421356 | 1.41420865 | +8.33e-9 |
| (-0.9,1.1,0) | 1.48323970 | 1.48323911 | +3.06e-10 |
| (-1.0,1.2,0) | 1.54919334 | 1.54919202 | +1.94e-10 |

The small differences between `q_inf` and `q_BPS` are consistent with the finite numerical tolerances of the locally executed BVP/integration pipeline. The interface tension at the analytic critical coupling is numerically zero at the displayed precision.

## Interpretation

This benchmark establishes that the code and normalization recover the standard one-component critical limit before any claim is made about the coupled neutral-scalar sector.

For `c != 0`, the scalar modes mix and the zero-interface-tension surface is shifted away from the one-component relation `q^2=2b`. The current research question is therefore not whether a Bogomolny point exists in ordinary GL theory, but how the additional neutral scalar modifies the interfacial critical surface and the large-winding corrections.
