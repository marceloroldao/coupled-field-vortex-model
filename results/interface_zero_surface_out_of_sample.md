# Out-of-sample validation of the local sigma=0 surface fit

Status: **numerical / locally reproduced; partial validation**.

Previously fitted local predictor:

`c_*(a,b) = -0.43021322 - 0.84923503 a + 0.05115560 b`.

Two parameter cuts not used in that fit were selected, the critical `c_*` was predicted first, and only then the nested numerical calculation was run: radial `n=1` BVP -> collective crossing `q_inf` -> planar Gibbs interface -> root of `sigma(q_inf)=0`.

| (a,b) | predicted c_* | numerical c_* | abs. error | q_inf at numerical c_* |
|---|---:|---:|---:|---:|
| (-0.85,1.05) | 0.34534994 | 0.34532650 | 2.34e-5 | 1.35266243 |
| (-0.95,1.15) | 0.43538900 | 0.43564681 | 2.58e-4 | 1.36685870 |

Both out-of-sample tests agree with the local affine approximation at the 1e-4--1e-5 absolute level in c_*.

Two additional planned cuts were not completed within the local execution budget and are therefore not counted as evidence.

Interpretation: within the currently explored neighborhood, the zero-interfacial-tension surface is well approximated by a plane in `(a,b,c)`. This remains a **local empirical parametrization**, not a derived global law. Broader-domain tests and/or an analytic reduction are still required.
