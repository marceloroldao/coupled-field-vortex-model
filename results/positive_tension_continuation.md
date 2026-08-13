# Positive-tension high-winding continuation test

Status: **numerical / locally reproduced**.

Parameter point:

`(a,b,c)=(-1.0,1.2,0.3)`.

Independent planar-interface analysis predicted

- `q_inf = 1.4798559943`
- `sigma(q_inf) > 0`
- leading asymptotic sign `q_c^(n)-q_inf > 0`
- `A_pred = +9.8520583e-4` in `q_c^(n)-q_inf ~ A/sqrt(n)+...`.

A direct high-winding BVP initially failed when winding number was doubled too aggressively. A continuation solver with smaller winding-number increments (`...16,20,24,28,32,...64,...128`) converged without relaxing the field equations or tolerance criteria.

Direct critical roots:

| n | q_c^(n) | q_c^(n)-q_inf | sqrt(n)*(q_c^(n)-q_inf) |
|---:|---:|---:|---:|
| 32 | 1.48023228098 | +3.76287e-4 | +2.12860e-3 |
| 64 | 1.48007679272 | +2.20798e-4 | +1.76639e-3 |
| 128 | 1.47999081469 | +1.34820e-4 | +1.52532e-3 |

Thus the **sign prediction is confirmed** at all three high-winding sectors: the finite-winding critical couplings approach the collective value from above, as predicted by positive planar interfacial tension.

Fitting the three roots to

`q_c^(n)-q_inf = A/sqrt(n)+B/n`

gives approximately

- `A_fit = +9.11409e-4`
- `B_fit = +6.87964e-3`.

The independently predicted leading coefficient was

`A_pred = +9.85206e-4`,

so the fitted and predicted A values differ by about 7.5 percent. This mirrors the earlier negative-tension base point, where the independent interface prediction reproduced the sign and magnitude of the high-winding correction to order ten percent.

Interpretation: the planar Gibbs interfacial tension acts as a parameter-dependent classifier for the leading finite-winding correction to the collective vortex-stability boundary. Positive and negative interface tensions produce opposite asymptotic approaches to `q_inf`.

Reproduction entry point: `simulations/positive_tension_continuation.py` (summary values) together with the project radial BVP conventions.
