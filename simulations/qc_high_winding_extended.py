"""Extended high-winding fusion-boundary scan.

This file records the locally reproduced roots for n=16,20,24,32,64,128 and
fits the large-n correction relative to the independently derived bag value.
The actual BVP implementation is in radial_vortex_solver.py / giant-vortex
variants used locally during development.
"""
import numpy as np

N=np.array([16,20,24,32,64,128],dtype=float)
QC=np.array([
  1.2823450021208787,
  1.2822856180749810,
  1.2822490744391220,
  1.2822078277947904,
  1.2821584946080210,
  1.2821446722518808,
])
QINF=1.2821745437
D=QC-QINF

# Fit high-n tail to A/sqrt(n)+B/n
X=np.column_stack([N**-0.5,N**-1])
coef=np.linalg.lstsq(X,D,rcond=None)[0]
pred=X@coef
rmse=np.sqrt(np.mean((pred-D)**2))
print('A_sqrt=',coef[0])
print('B_n=',coef[1])
print('rmse=',rmse)
for n,q,d,p in zip(N,QC,D,pred):
    print(f'n={int(n):3d} qc={q:.12f} delta={d:+.12e} fit={p:+.12e}')
