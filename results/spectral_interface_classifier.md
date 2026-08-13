# Spectral diagnostics on the zero-interface-tension surface

Status: **numerical / locally reproduced; classifier candidate**.

For accumulated points satisfying `sigma=0`, compute the scalar Hessian around the mixed vacuum,

`M_s^2 = 2 [[b v^2, c v X0], [c v X0, X0^2]]`,

its eigenmasses `m_- < m_+`, the light-mode mixing angle `alpha`, and the gauge mass

`m_A = sqrt(2) q_inf v`.

Across nine currently available zero-tension points:

- `m_A` has mean about `0.9981` with relative standard deviation about `0.49%`;
- `m_-` has relative standard deviation about `0.77%`;
- `m_+` about `1.31%`;
- `m_-/m_+` about `0.69%`;
- the mixing angle varies substantially and is not itself approximately constant.

A first correction to the simple `m_A ~= 1` rule is obtained by fitting

`m_A = c0 + c1 alpha + c2 (m_-/m_+)`.

For the current sample,

`c0 ~= 0.77708`, `c1 ~= 0.04915`, `c2 ~= 0.38992`.

The in-sample RMSE is about `3.5e-4`; leave-one-out RMSE is about `5.5e-4`, with maximum leave-one-out error about `1.0e-3`.

This is significantly tighter than the single-variable `m_A ~= 1` approximation, but the sample is still too small to claim a universal spectral law. The current interpretation is that zero planar interfacial tension is primarily set by the gauge mass scale, with corrections from scalar-mode mixing and the scalar mass ratio.

Next step: validate the spectral relation on additional independently located `sigma=0` points and compare against known single-component Bogomolny/GL criticality conditions.
