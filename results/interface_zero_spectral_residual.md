# Spectral residual on the zero-interface-tension surface

Status: **numerical / locally reproduced; candidate approximation tested out of sample**.

Candidate criterion on the surface `sigma=0`:

`q_inf^2 * (-(a+c)) / (b-c^2) = 1`,

equivalently `q_inf v = 1/sqrt(2)` in the present normalization.

Define the residual

`R = q_inf^2 * (-(a+c)) / (b-c^2) - 1`.

Two additional sigma-zero cuts outside the original local fit region were solved with the same radial and planar-interface conventions:

| a | b | c* | q_inf | R |
|---:|---:|---:|---:|---:|
| -0.75 | 0.95 | 0.254139 | 1.324422 | -1.765e-2 |
| -0.85 | 1.15 | 0.348512 | 1.423053 | -1.263e-2 |

These residuals are small but clearly nonzero at the 1--2 percent level. Therefore `q_inf v = 1/sqrt(2)` is **not supported as an exact identity** by the expanded sample. It remains a useful local approximation near the previously studied region.

Interpretation: the zero-surface-tension condition is controlled predominantly by the gauge mass scale and vacuum combinations `(a+c)` and `(b-c^2)`, but scalar mixing and full interface-profile relaxation shift the boundary away from the single-component-like spectral condition.

Scientific status: retain as `candidate approximation`, not `derived law`.
