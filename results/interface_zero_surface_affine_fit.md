# Preliminary affine representation of the zero-interfacial-tension surface

Status: **numerical / candidate parametrization**.

The zero of the planar Gibbs interfacial tension, evaluated at the collective crossing `q_inf(a,b,c)`, defines a codimension-one surface in `(a,b,c)`.

Five locally reproduced cuts are currently available:

| a | b | c_* |
|---:|---:|---:|
| -0.8 | 1.0 | 0.29990234 |
| -0.9 | 1.1 | 0.39063965 |
| -1.0 | 1.2 | 0.48056641 |
| -0.9 | 1.0 | 0.38583984 |
| -1.0 | 1.1 | 0.47470703 |

The first three points happen to lie on the line `b=-a+0.2`; by themselves they cannot determine a two-dimensional surface.  Two additional independent cuts remove this degeneracy.

A least-squares affine fit gives

`c_*(a,b) ~= -0.430213 - 0.849235 a + 0.051156 b`

or, equivalently,

`c_*(a,b) ~= -0.430213 + 0.849235(-a) + 0.051156 b`.

In-sample RMSE is about `4.4e-4`.  Leave-one-out RMSE is about `1.2e-3`, so this should be treated only as a compact local approximation, not a derived law.

One additional attempted cut at `(-0.8,1.1)` did not converge within the planar-interface mesh budget and is excluded from the fit.

Interpretation: over the sampled domain, the location of `sigma=0` is much more sensitive to `a` than to `b`; however, the data set is still too small to establish whether the surface is genuinely close to affine or merely locally smooth.

Next step: add several off-line cuts spanning independent changes in `a` and `b`, then test affine versus quadratic parametrizations on held-out points.
