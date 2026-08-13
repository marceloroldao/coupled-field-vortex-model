"""Check the asymptotic giant-vortex correction predicted by planar interface tension.

Uses independently reproduced quantities at (a,b,c)=(-0.8,1,0.4):
q_inf, sigma(q_inf), d/dq[e_bulk-E1], and high-winding q_c values.
"""
import numpy as np

QINF=1.2821745437
SIGMA=-3.925746789433e-05
FPRIME=-0.690840291982292
DELTA_V=1/21

# R_n = geom*sqrt(n) at leading bag order.
geom=np.sqrt(np.sqrt(2)/(QINF*np.sqrt(DELTA_V)))
C=2*np.pi*SIGMA*geom
A_PRED=-C/FPRIME
print('A_pred =',A_PRED)

N=np.array([32.,64.,128.])
QC=np.array([1.2822078278,1.2821584946,1.2821446723])
delta=QC-QINF

# Infer the next B/n term after fixing A from the independent interface calculation.
B_each=N*(delta-A_PRED/np.sqrt(N))
B=B_each.mean()
print('B_each =',B_each)
print('B_mean =',B)

pred=QINF+A_PRED/np.sqrt(N)+B/N
for n,obs,est in zip(N,QC,pred):
    print(int(n),obs,est,obs-est)

# Also allow C/n^(3/2) to quantify residual curvature/profile relaxation.
X=np.column_stack([N**-1,N**-1.5])
rhs=delta-A_PRED*N**-0.5
B2,C2=np.linalg.lstsq(X,rhs,rcond=None)[0]
pred2=QINF+A_PRED*N**-0.5+B2/N+C2/N**1.5
rmse=np.sqrt(np.mean((QC-pred2)**2))
print('B,C =',B2,C2,'rmse =',rmse)
