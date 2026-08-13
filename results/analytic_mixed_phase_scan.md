# Mixed-phase analytic scan — local validation

Status: **numerical + derived**  
Execution environment: local ChatGPT Python runtime (not GitHub Actions)  
Date: 2026-08-12 America/Sao_Paulo

## Scope

The scan checks the stable mixed phase of the dimensionless coupled-field model using the parameter grid:

- `a`: 81 points in `[-2.0, 0.5]`
- `b`: 61 points in `[0.1, 2.0]`
- `c`: 61 points in `[-1.2, 1.2]`

Only points with a positive mixed vacuum and positive scalar Hessian eigenvalues are retained.

## Reference point

For `(a,b,c)=(-0.8,1.0,0.4)`:

- `m_- = 0.8291749486`
- `m_+ = 1.3725514475`
- `v = 0.6900655593`
- `X0 = 0.8997354108`

These reproduce the values used in the exploratory analysis.

## Grid results

Valid stable mixed-phase points: **167,023**.

### Hessian determinant identity

Checked:

`det(M_s^2) = 4 v^2 X0^2 (b-c^2)`

Maximum relative discrepancy over the retained grid:

`8.81e-12`

Classification: **derived identity numerically verified**.

### Approximate molecular-window ordering

Using

`q_LR = m_-/v`

and the adiabatic estimate

`q_c = sqrt(2 (b-c^2))`,

the scan found **0 violations** of

`q_LR <= q_c`

across all 167,023 retained points. The minimum numerical gap was approximately machine zero (`-4.44e-16`) and the largest sampled gap was `1.37003`.

Classification: **candidate relation strongly supported within the scanned mixed-phase domain**.

## Interpretation limits

The `q_c` expression is derived from the adiabatic effective quartic `b_eff=b-c^2`; it is not yet an exact theorem for the fully nonlinear vortex fusion boundary. Therefore this scan validates the analytic ordering of the approximate classifier, not the full statement `E_2-2E_1=0`.

The next required validation is a radial vortex solver for `n=1,2,3`, with box/grid convergence, followed by comparison of the measured nonlinear fusion boundary against the analytic estimate.

## Reproduction

Run:

```bash
python simulations/analytic_mixed_phase_scan.py
```

GitHub Actions reproduction is intentionally pending until CI capacity is available.
