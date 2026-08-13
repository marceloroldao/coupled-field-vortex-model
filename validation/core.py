"""Shared analytic and numerical definitions for validation v0.1.

The functions in this module use the action and normalizations documented in
``theory/MODEL.md``; validation code must not tune them to expected results.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_bvp


@dataclass(frozen=True)
class Parameters:
    a: float = -0.8
    b: float = 1.0
    c: float = 0.4


def mixed_vacuum(p: Parameters) -> tuple[float, float]:
    d = p.b - p.c**2
    if d <= 0:
        raise ValueError("mixed branch requires b-c^2>0")
    v2 = -(p.a + p.c)/(2*d)
    x2 = (p.b + p.a*p.c)/d
    if v2 <= 0 or x2 <= 0:
        raise ValueError("parameters are outside the mixed-vacuum region")
    return float(np.sqrt(v2)), float(np.sqrt(x2))


def scalar_hessian(p: Parameters) -> np.ndarray:
    psi0, x = mixed_vacuum(p)
    # The canonically normalized charged radial field is h=sqrt(2) delta|psi|.
    # This is exactly the convention v=sqrt(2)|psi_0| in theory/MODEL.md.
    return np.array([[4*p.b*psi0*psi0, 2*np.sqrt(2)*p.c*psi0*x],
                     [2*np.sqrt(2)*p.c*psi0*x, 2*x*x]])


def scalar_masses(p: Parameters) -> tuple[float, float]:
    eigenvalues = np.linalg.eigvalsh(scalar_hessian(p))
    return tuple(float(np.sqrt(x)) for x in eigenvalues)


def solve_universal(rho_x: float, length: float = 12.0, points: int = 500,
                    tol: float = 1e-6):
    """Solve the rescaled BPS profile and first-order response system.

    Finite-box asymptotic conditions are

    F(-L)=0, G'(-L)=1, F(+L)=1, G(+L)=0,
    P(-L)=0, R'(-L)=-1, P(+L)=-1/2, R(+L)=0,
    U(-L)=0, U(+L)=-1.

    These are the asymptotic conditions obtained from the first-order expansion
    about the c=0 Bogomolny interface.  In particular, the charged response
    (P,R) must not be forced to vanish at both ends.
    """
    if rho_x <= 0:
        raise ValueError("rho_X must be positive")
    z = np.linspace(-length, length, points)
    s = .5*(1+np.tanh(z))
    F = s
    G = (z-length)*(1-s)
    P = -.5*s
    R = -(z-length)*(1-s)
    U = -s
    y = np.vstack((F, np.gradient(F,z), G, np.gradient(G,z),
                   P, np.gradient(P,z), R, np.gradient(R,z),
                   U, np.gradient(U,z)))

    def ode(_, y):
        F,Fp,G,Gp,P,Pp,R,Rp,U,Up = y
        return np.vstack((Fp, G*G*F+(F*F-1)*F, Gp, 2*F*F*G,
            Pp, (G*G-1+3*F*F)*P+2*G*F*R+F,
            Rp, 4*G*F*P+2*F*F*R, Up, (U+F*F)/rho_x))

    def bc(left,right):
        return np.array((left[0], left[3]-1, right[0]-1, right[2],
                         left[4], left[7]+1, right[4]+.5, right[6],
                         left[8], right[8]+1))

    return solve_bvp(ode, bc, z, y, tol=tol, max_nodes=50000)
