import math
import numpy as np
import pytest

from validation.core import Parameters, mixed_vacuum, scalar_hessian, scalar_masses


def test_reference_vacuum_and_mass_determinant():
    p = Parameters()
    psi0, x0 = mixed_vacuum(p)
    assert math.isclose(psi0**2, -(p.a+p.c)/(2*(p.b-p.c**2)))
    assert math.isclose(x0**2, (p.b+p.a*p.c)/(p.b-p.c**2))
    expected = 8*psi0**2*x0**2*(p.b-p.c**2)
    assert np.linalg.det(scalar_hessian(p)) == pytest.approx(expected)
    assert scalar_masses(p)[0] > 0


@pytest.mark.parametrize("p", [Parameters(-.8,.16,.4), Parameters(.2,1,.1)])
def test_invalid_mixed_vacua_are_rejected(p):
    with pytest.raises(ValueError):
        mixed_vacuum(p)
