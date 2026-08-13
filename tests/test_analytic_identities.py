import math
import numpy as np

from simulations.analytic_mixed_phase_scan import mixed_masses


def test_reference_masses():
    result = mixed_masses(-0.8, 1.0, 0.4)
    assert result is not None
    m_minus, m_plus, v, x0, _ = result
    assert math.isclose(m_minus, 0.8291749485696821, rel_tol=1e-12)
    assert math.isclose(m_plus, 1.3725514475213803, rel_tol=1e-12)
    assert math.isclose(v, 0.6900655593423543, rel_tol=1e-12)
    assert math.isclose(x0, 0.8997354108424374, rel_tol=1e-12)


def test_hessian_determinant_identity_reference():
    a, b, c = -0.8, 1.0, 0.4
    result = mixed_masses(a, b, c)
    assert result is not None
    _, _, v, x0, matrix = result
    expected = 4.0 * v * v * x0 * x0 * (b - c * c)
    assert math.isclose(float(np.linalg.det(matrix)), expected, rel_tol=1e-12)


def test_approximate_window_ordering_reference():
    a, b, c = -0.8, 1.0, 0.4
    result = mixed_masses(a, b, c)
    assert result is not None
    m_minus, _, v, _, _ = result
    q_lr = m_minus / v
    q_c = math.sqrt(2.0 * (b - c * c))
    assert q_lr < q_c
