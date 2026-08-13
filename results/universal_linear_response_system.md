# Universal first-order response system around the BPS interface

Status: **derived + numerically verified**.

For small neutral-scalar coupling `c`, expand the planar interface fields at fixed `q=q_BPS=sqrt(2b)` as

`f=f0+c p+O(c^2)`,

`A=A0+c r+O(c^2)`,

`X=1+c eta+O(c^2)`.

The first-order static equations are

`p'' = [q^2 A0^2 + a + 6 b f0^2] p + 2 q^2 A0 f0 r + f0`,

`r'' = 4 q^2 A0 f0 p + 2 q^2 f0^2 r`,

`eta'' = 2 eta + 2 f0^2`.

The broken-phase boundary conditions shift at first order, so the charged-sector response cannot be omitted when computing the full O(c^2) interfacial free-energy correction.

Define `s=-a>0`, `v0^2=s/(2b)`, `y=sqrt(s) z`, and the dimensionless fields

`f0=v0 F`,

`A0=sqrt(s)/q * G`,

`p=(v0/s) P`,

`r=[1/(q sqrt(s))] R`,

`eta=v0^2 U`.

At the BPS point the background becomes universal:

`F'' = G^2 F + (F^2-1)F`,

`G'' = 2 F^2 G`,

with `F(-inf)=0`, `G'(-inf)=1`, `F(+inf)=1`, `G(+inf)=0`.

The charged first-order response is also universal:

`P'' = (G^2-1+3F^2)P + 2GFR + F`,

`R'' = 4GFP + 2F^2 R`,

with `P(-inf)=0`, `R'(-inf)=-1`, `P(+inf)=-1/2`, `R(+inf)=0`.

The neutral response contains the only remaining mass-ratio parameter:

`U'' = (U+F^2)/rho_X`,

where

`rho_X = m_h^2/m_X^2 = -a/2`,

with `U(-inf)=0`, `U(+inf)=-1`.

Therefore the full O(c) response is organized by a universal BPS background, a universal charged-sector response `(P,R)`, and a one-parameter neutral response `U_{rho_X}`. This explains why the O(c^2) critical-coupling correction collapses to a function `C(rho_X)` rather than a generic function of `a` and `b`.

Numerical checks:

- BPS background and charged response converged with `solve_bvp` at tight tolerance.
- For fixed `a=-0.8` and `b=0.9,1.0,1.3`, normalized BPS and neutral-response profiles agree at the `~10^-8` level after translation alignment.
- Representative neutral response values at the interface center vary smoothly with `rho_X`: approximately `-0.2930` at `rho_X=0.30`, `-0.3014` at `0.40`, `-0.3084` at `0.50`, and `-0.3145` at `0.60`.

Important correction to earlier intermediate reasoning: the neutral response alone is **not** sufficient to reconstruct the complete coefficient `C(rho_X)`. The charged amplitude and gauge field both respond at O(c) and contribute to the O(c^2) Gibbs interfacial energy. The v0.1 derivation must therefore use the full `(P,R,U)` linear-response system.
