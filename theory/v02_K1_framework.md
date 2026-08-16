# V0.2 — Framework for the K1 curvature coefficient

## Purpose

The two-term prediction uses independently computed planar tension `sigma` and an exploratory constant sector `A0`. The remaining high-winding residual decreases with n, but the coefficient of the next term must be derived from the field functional rather than fitted to giant-vortex data.

The wall expansion is

G_wall(R) = 2 pi R sigma + 2 pi A0 + (2 pi/R) K1 + O(R^-2).

Since R_n ~ sqrt(C_R n), the K1 contribution to energy per flux scales as n^(-3/2), and therefore contributes to the critical boundary at the same order after linearization around q_inf.

## 1. Profile expansion

Write

Phi_R = Phi_0 + R^-1 Phi_1 + R^-2 Phi_2 + ...

for Phi=(f,X,h). The first response satisfies

L Phi_1 = S_1[Phi_0],

with zero modes fixed by the chosen dividing-surface and gauge conditions.

At the next order,

L Phi_2 = S_2[Phi_0,Phi_1],

where S_2 contains explicit second-order geometry and quadratic terms in Phi_1.

## 2. Structure of K1

Expanding the exact circular Gibbs functional gives

K1 = int [x g_1 + g_2] dx,

provided the same bulk subtraction, ensemble, gauge convention, and dividing surface are used at every order.

The second-order density g_2 contains three conceptually distinct pieces:

1. explicit second-order geometry from the cylindrical measure and magnetic sector;
2. terms linear in Phi_2;
3. quadratic terms in Phi_1.

On shell, the Phi_2-linear contribution should reduce to boundary/constraint terms after using the planar Euler-Lagrange equations. Therefore the calculable core of K1 is expected to be expressible using Phi_0 and Phi_1 plus explicit geometry, but this must be proven for the exact Gibbs ensemble used here.

## 3. Independent route

The allowed V0.2 route is:

1. solve the planar interface for Phi_0;
2. construct the full linear operator L and curvature source S_1;
3. solve L Phi_1=S_1 with fixed zero-mode conventions;
4. evaluate the derived K1 functional;
5. test domain, mesh, tolerance, and dividing-surface stability;
6. only then compare the resulting n^(-3/2) contribution against held-out giant-vortex data.

No giant-vortex q_c^(n) value may enter steps 1–4.

## 4. Critical-boundary coefficient

If

E_n/n = E_inf(q) + beta_sigma n^-1/2 + beta_1 n^-1 + beta_3over2 n^-3/2 + ...,

then linearization of F(q)=E_inf(q)-E_1(q) gives

q_c^(n)-q_inf = alpha_sigma n^-1/2 + alpha_1 n^-1 + alpha_3over2 n^-3/2 + ...,

with

alpha_3over2 = - beta_3over2 / F'(q_inf).

For a pure K1 wall contribution,

beta_3over2 = 2 pi K1 / sqrt(C_R),

so the candidate mapping is

alpha_3over2 = - [2 pi K1 / sqrt(C_R)] / F'(q_inf),

subject to completion of the ensemble/boundary derivation.

## 5. Current status

DERIVED STRUCTURALLY:

- the order at which K1 enters the circular wall expansion;
- the expected n^(-3/2) scaling if K1 is the next surviving coefficient;
- the no-fit route from planar response to a giant-vortex prediction.

NOT YET DERIVED:

- the complete model-specific S_1 including all boundary/ensemble pieces;
- the final gauge/dividing-surface invariant K1 functional;
- proof that Phi_2-linear terms cancel or reduce to controlled boundary terms;
- the numerical value of K1.

Therefore K1 remains INCOMPLETE.

## 6. Scientific and technological relevance if closure succeeds

### Science

A successful derivation would provide a controlled three-level hierarchy linking planar tension, constant curvature response, and next-order curvature response to finite-winding vortex criticality. This would strengthen effective-interface descriptions of topological defects and multifield phase boundaries.

### Technology

If later calibrated to experimentally relevant superconductors, a three-term asymptotic model could estimate large-winding flux structures much faster than repeated full radial boundary-value solves. That could support parameter sweeps for trapped flux, vortex stability, and superconducting-device modeling. These are conditional applications, not current device claims.
