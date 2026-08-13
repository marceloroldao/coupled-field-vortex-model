# Radial vortex energy boundary — local reproduction

Status: **numerical / locally reproduced**. GitHub Actions reproduction pending.

Model parameters:

- `a = -0.8`
- `b = 1.0`
- `c = 0.4`
- mixed vacuum branch

Solver: `scipy.integrate.solve_bvp`, axisymmetric sectors `n=1,2,3`.

## Energy scan

| q | E1 | E2 | E3 | Delta2 = E2-2E1 | Delta3 = E3-3E1 |
|---:|---:|---:|---:|---:|---:|
| 1.25 | 1.5283225536 | 3.0676590474 | 4.6092845931 | +0.0110139403 | +0.0243169324 |
| 1.27 | 1.5182918447 | 3.0413866832 | 4.5648642662 | +0.0048029939 | +0.0099887322 |
| 1.28 | 1.5133643303 | 3.0285003515 | 4.5430932952 | +0.0017716910 | +0.0030003044 |
| 1.29 | 1.5084938971 | 3.0157761347 | 4.5216070742 | -0.0012116596 | -0.0038746172 |
| 1.30 | 1.5036794722 | 3.0032108072 | 4.5003997791 | -0.0041481372 | -0.0106386374 |

Root refinement using the same solver gives:

- `q_c^(2) = 1.2859194383` from `E2-2E1 = 0`
- `q_c^(3) = 1.2843440857` from `E3-3E1 = 0`

The two thresholds are close but measurably distinct. This means the simple adiabatic estimate of one universal `q_c` is only an approximation; nonlinear core physics introduces a weak winding-number dependence.

## Convergence check near the boundary

At `q=1.285`, the calculation was repeated over radii `R = 14, 18, 22, 28` and initial meshes of `300, 500, 800` points. All BVP solves converged.

Across that grid/box sweep, energies were stable at roughly the 8th–9th decimal place. Representative values:

- `R=14, N=300`: `Delta2 = +2.7411286e-4`, `Delta3 = -4.5111772e-4`
- `R=28, N=800`: `Delta2 = +2.7408895e-4`, `Delta3 = -4.5118148e-4`

The sign difference at `q=1.285` is therefore resolved numerically rather than caused by the tested box/mesh choices.

## Interpretation

For this parameter point:

- below `q_c^(3)`, both `n=2` and `n=3` axial fusion are energetically disfavored relative to separated `n=1` vortices;
- between `q_c^(3)` and `q_c^(2)`, the `n=3` axial sector is already favored while `n=2` is still slightly disfavored;
- above `q_c^(2)`, both are favored.

This small split is a useful nonlinear benchmark for any spectral classifier developed later.
