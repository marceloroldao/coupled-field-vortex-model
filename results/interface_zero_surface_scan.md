# Zero-interfacial-tension surface at the collective crossing

Status: **numerical / locally reproduced; partial parameter-space map**.

For each valid mixed-vacuum parameter point, define `q_inf(a,b,c)` by the large-winding bulk crossing

`2*pi*sqrt(2*DeltaV)/q = E1(q)`.

At that coupling, solve the planar Gibbs interface between the normal core phase and the mixed superconducting phase.  The hypersurface

`sigma(a,b,c; q_inf(a,b,c)) = 0`

separates regions with opposite leading high-winding corrections

`q_c^(n)-q_inf ~ A/sqrt(n)`, with `sign(A)=sign(sigma)` for the tested cases.

## Resolved cuts

| fixed (a,b) | c_* at sigma=0 | q_inf(c_*) |
|---|---:|---:|
| (-0.8, 1.0) | 0.29990 | 1.34033 |
| (-0.9, 1.1) | 0.39064 | 1.36144 |
| (-1.0, 1.2) | 0.48057 | 1.36885 |

For the middle cut `(a,b)=(-0.9,1.1)`, the coarse scan showed

- `c=0.35`: positive interfacial tension;
- `c=0.40`: negative interfacial tension,

and bisection refined the zero to approximately `c_*=0.39064`.

## Interpretation

The zero is not a universal numerical constant.  It moves appreciably with `(a,b)`, so the relevant object is a codimension-one surface in the model parameter space.  Crossing that surface reverses the sign of the leading finite-winding correction to the multiquanta-vortex fusion boundary.

This provides a conventional field-theory phase-boundary interpretation of the earlier high-winding results: the planar interfacial tension acts as an asymptotic classifier for multiquanta-vortex stability.

Further cuts are required before fitting an analytic approximation to the full surface.
