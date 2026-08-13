"""Fit finite-winding corrections to the large-n fusion boundary.

Uses locally reproduced q_c^(n) values and the independently derived bag-limit
q_c^(infinity).  This script does not run the radial BVP; it analyzes its output.
"""
import numpy as np
from scipy.optimize import curve_fit

N = np.array([2,3,4,5,6,8,10,12], dtype=float)
QC = np.array([1.28591955,1.28434393,1.28362384,1.28322810,1.28298327,
               1.2827023687,1.2825490774,1.2824542123])
QINF = 1.2821745437
D = QC-QINF

def power(n,A,p):
    return A*n**(-p)

pars,_ = curve_fit(power,N,D,p0=[0.01,1.0],maxfev=10000)
pred=power(N,*pars)
rmse=np.sqrt(np.mean((pred-D)**2))
print(f"free-power: A={pars[0]:.12g}, p={pars[1]:.12g}, rmse={rmse:.12g}")

for p in (0.5,1.0,1.5,2.0):
    x=N**(-p)
    A=float(x@D/(x@x))
    e=np.sqrt(np.mean((A*x-D)**2))
    print(f"p={p:g}: A={A:.12g}, rmse={e:.12g}")

for name,X in [
    ("n^-1/2+n^-1",np.column_stack([N**-0.5,N**-1])),
    ("n^-1+n^-2",np.column_stack([N**-1,N**-2])),
    ("n^-1/2+n^-1+n^-3/2",np.column_stack([N**-0.5,N**-1,N**-1.5])),
]:
    coef=np.linalg.lstsq(X,D,rcond=None)[0]
    e=np.sqrt(np.mean((X@coef-D)**2))
    print(name, "coeff=", coef, "rmse=", e)
