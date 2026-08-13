# Winding-dependent fusion thresholds

Status: **numerical / locally reproduced**

Parameters:

- a = -0.8
- b = 1.0
- c = 0.4
- radial gauge vortex solver

Critical coupling q_c^(n) is defined by

`E_n - n E_1 = 0`.

## Results

| n | q_c^(n) |
|---:|---:|
| 2 | 1.28591955 |
| 3 | 1.28434393 |
| 4 | 1.28362384 |
| 5 | 1.28322810 |
| 6 | 1.28298327 |

The sequence is monotone decreasing over n=2..6.

## Convergence checks

For n=4,5,6 the roots were recomputed with (R,N) = (18,450), (24,650), (30,850). The maximum spread was below 1.3e-7.

## Preliminary asymptotic fit

A fit `q_c(n)=q_inf+A/n` gives `q_inf ~ 1.28145`.
A fit `q_c(n)=q_inf+A/n+B/n^2` gives `q_inf ~ 1.28184`.

These are **candidate extrapolations**, not final asymptotic results.

## Interpretation

The fusion threshold is not exactly universal in winding number. The simple adiabatic estimate `q_c^2 ~ 2(b-c^2)` remains useful as a first approximation, but nonlinear core physics introduces a small n-dependence. The next test is to extend to larger n and determine whether q_c^(n) converges to a stable collective limit.
