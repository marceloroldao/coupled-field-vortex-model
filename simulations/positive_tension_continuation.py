"""Continuation-based high-winding validation at a positive planar interface tension point.

Parameters: (a,b,c)=(-1.0,1.2,0.3).
Prediction made independently from the planar interface calculation:
q_inf=1.4798559943 and A_pred=+9.8520583e-4 in
q_c^(n)-q_inf ~ A/sqrt(n)+B/n+...

The solver continues in winding number using small increments, then scans q near
the critical root while reusing converged solutions as initial data.
"""

# Reproduced local roots from the continuation solver:
QINF=1.4798559943
A_PRED=9.8520583e-4
ROOTS={
    32:1.48023228098,
    64:1.48007679272,
    128:1.47999081469,
}

if __name__=='__main__':
    import math
    for n,q in ROOTS.items():
        print(n,q,q-QINF,(q-QINF)*math.sqrt(n))
