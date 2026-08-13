# Multi-parameter collective/interface pre-screen

Status: **numerical / locally reproduced; partial domain scan**.

Purpose: test whether the interface-to-giant-vortex mechanism found at the base point is structurally available away from `(a,b,c)=(-0.8,1,0.4)` without modifying the master model.

For each valid mixed-vacuum point, first solve the radial `n=1` BVP and locate the collective bag crossing from

`2*pi*sqrt(2*DeltaV)/q = E1(q)`.

Then solve the planar Gibbs interface at that independently determined `q_inf`, compute `sigma(q_inf)`, and predict the leading high-winding shift coefficient `A` in

`q_c^(n)-q_inf = A/sqrt(n)+...`.

| (a,b,c) | q_inf | sigma(q_inf) | A_pred |
|---|---:|---:|---:|
| (-0.6,1.0,0.2) | 1.38252020 | -5.75e-6 | -1.46e-4 |
| (-1.0,1.2,0.3) | 1.47985599 | +7.29e-5 | +9.85e-4 |
| (-0.7,0.9,0.5) | 1.12611477 | -6.25e-5 | -2.45e-3 |
| (-0.5,0.8,0.25) | 1.21063161 | solver not converged | pending |

The sign is **not universal**.  In particular, the point `(-1.0,1.2,0.3)` has positive planar interface tension at its collective crossing and therefore predicts approach to `q_inf` from above at leading `1/sqrt(n)` order.  The other two converged non-base points predict approach from below, with substantially different amplitudes.

This is useful: the master equation does not force one qualitative finite-winding pattern.  Instead the planar interface provides a parameter-dependent classifier for the asymptotic giant-vortex correction.

Next validation step: run direct high-winding radial roots (e.g. n=32,64,128) at these non-base points and compare fitted A with the independently predicted values above.  The fourth point remains pending because the planar-interface BVP exceeded the mesh-node budget; it is not counted as evidence.
