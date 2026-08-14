import numpy as np
from scipy.integrate import simpson


def test_radial_magnetic_identity_for_h_variable():
    q = 1.7
    n = 5
    r = np.linspace(0.4, 4.0, 2000)
    h = 0.3*np.exp(-r) + 0.05*r
    hp = -0.3*np.exp(-r) + 0.05
    Aphi = h + n/(q*r)
    Aphi_p = hp - n/(q*r*r)
    B_direct = Aphi_p + Aphi/r
    B_h = hp + h/r
    assert np.max(np.abs(B_direct-B_h)) < 1e-12


def test_first_moment_origin_shift_identity():
    z = np.linspace(-8.0, 8.0, 20001)
    g = np.exp(-z*z) * (1.0 + 0.1*z)
    sigma = simpson(g, x=z)
    m1 = simpson(z*g, x=z)
    delta = 0.73
    m1_shift = simpson((z-delta)*g, x=z)
    assert abs((m1_shift-m1) + delta*sigma) < 1e-11
