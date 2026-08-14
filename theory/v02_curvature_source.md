# V0.2 G1 — Model-specific curvature source

## 1. Gauge-invariant local variable

For the radial ansatz

psi = f(r) exp(i n theta),
A = A_phi(r) e_theta,
X = X(r),

introduce

h(r) = A_phi(r) - n/(q r).

Then

n/r - q A_phi = -q h

and the magnetic field is exactly

B = A_phi' + A_phi/r = h' + h/r.

This variable is useful because its planar limit is the same tangential gauge potential used by the planar-interface solver, up to an irrelevant overall sign convention fixed here so that h' tends to the magnetic field on the normal side.

## 2. Exact radial equations in h

The radial equations become

f'' + f'/r
= q^2 h^2 f + (a + 2 b f^2 + c X^2) f,

X'' + X'/r
= (-1 + X^2 + 2 c f^2) X,

h'' + h'/r - h/r^2
= 2 q^2 f^2 h.

Let r = R + x and epsilon = 1/R. Expand

f = f0 + epsilon f1 + O(epsilon^2),
X = X0 + epsilon X1 + O(epsilon^2),
h = h0 + epsilon h1 + O(epsilon^2).

Since

1/(R+x) = epsilon + O(epsilon^2),
1/(R+x)^2 = O(epsilon^2),

the h/r^2 term does not enter the first curvature source.

## 3. Planar equations

At O(epsilon^0):

f0'' = q^2 h0^2 f0 + (a + 2 b f0^2 + c X0^2) f0,

X0'' = (-1 + X0^2 + 2 c f0^2) X0,

h0'' = 2 q^2 f0^2 h0.

These are exactly the equations solved in `simulations/planar_interface_tension.py`.

## 4. First curvature response

At O(epsilon), the response obeys a coupled linear system.

For f1:

f1''
- [q^2 h0^2 + a + 6 b f0^2 + c X0^2] f1
- 2 c f0 X0 X1
- 2 q^2 h0 f0 h1
= -f0'.

For X1:

X1''
- [-1 + 3 X0^2 + 2 c f0^2] X1
- 4 c f0 X0 f1
= -X0'.

For h1:

h1''
- 2 q^2 f0^2 h1
- 4 q^2 f0 h0 f1
= -h0'.

In operator notation,

L Phi1 = S,

with

Phi1 = (f1, X1, h1)^T

and the **model-specific first geometric curvature source**

S = -(f0', X0', h0')^T.

This is the first closure that was missing from the generic G1 note: at order 1/R, cylindrical geometry drives the planar wall through the translation-direction derivatives of the three planar profiles. The separate h/r^2 gauge term enters only at O(1/R^2).

## 5. Gibbs functional and explicit O(1/R) density

At the thermodynamic critical field Hc, use the bulk-subtracted radial Gibbs density

g_R = f'^2 + q^2 h^2 f^2 + (1/2) X'^2
    + (1/2) (h' + h/r)^2
    + V(f,X) - Hc (h' + h/r) - Vmix.

The radial wall contribution is

G_wall = 2 pi int (R+x) g_R dx.

Holding the planar profiles fixed while expanding the explicit geometric factors gives

B = h0' + epsilon h0 + O(epsilon^2)

and therefore the explicit first-curvature contribution to the local Gibbs density is

g_geom,1 = h0 (h0' - Hc).

Combining this with the circular measure gives the constant-in-R wall coefficient candidate

A0 = int [x g0(x) + h0(x)(h0'(x)-Hc)] dx

plus any surviving boundary/ensemble contribution from the first variation.

The ordinary bulk first variation proportional to Phi1 vanishes on shell if the planar Euler-Lagrange equations and admissible boundary conditions are used. Therefore the remaining task is not to fit Phi1, but to verify carefully that no boundary/ensemble term has been omitted and to test A0 numerically under domain, mesh, and convention changes.

## 6. Important critical-point simplification

Under a simple translation of the chosen normal-coordinate origin,

x -> x - delta,

the first moment transforms as

int x g0 dx -> int x g0 dx - delta sigma,

where

sigma = int g0 dx.

Hence exactly at a zero-tension point, sigma = 0, the first-moment part is invariant under this coordinate-origin shift. This makes the asymptotic critical interface especially useful for testing the candidate constant curvature coefficient.

This statement concerns coordinate-origin shifts of the postprocessed planar profile. A complete physical dividing-surface invariance test must also track the flux/radius convention in h and remains part of G2.

## 7. Current classification

**Newly derived:** the exact local gauge variable h, exact radial equations in h, the explicit first curvature source S, and the explicit geometric Gibbs-density term h0(h0'-Hc).

**Still incomplete:** proof that all boundary/ensemble contributions vanish or are included; numerical convergence of A0; invariant mapping from A0 to the giant-vortex observable; held-out prediction.

G1 is therefore advanced substantially but remains **INCOMPLETE** until the boundary/ensemble accounting is closed.

## 8. Impact potential — science and technology

### Science

- **Superconducting vortex theory:** gives a concrete, non-fitted route from a planar normal/superconducting interface to curvature corrections of large-flux vortices.
- **Near-Bogomolny physics:** the zero-tension regime is precisely where subleading curvature terms can determine whether large vortices favor fusion or separation, so isolating A0 can sharpen the type-I/type-II crossover analysis.
- **Multicomponent order parameters:** the source shows explicitly how the neutral field X participates in curvature response rather than entering only through a scalar correction to surface tension.
- **Defect asymptotics:** the same Hessian-plus-geometric-source construction can be reused for circular domain walls, bubbles, and related multifield defects.

### Technology

- **Flux management in superconductors:** if validated against a material-calibrated regime, curvature corrections can improve models of large trapped-flux structures and vortex stability.
- **Superconducting device simulation:** a reduced curvature model may eventually accelerate design calculations where full nonlinear vortex solves are too expensive.
- **Numerical engineering:** the independent planar-response route could provide surrogate asymptotics for large-winding parameter sweeps, reducing computation while retaining controlled error estimates.

All technological implications remain conditional on G2–G5 validation and later experimental/material calibration.
