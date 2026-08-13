"""Planar normal/mixed interface tension at thermodynamic critical field.

Model parameters default to the reference point a=-0.8, b=1, c=0.4.
The interface connects (psi=0,X=1,B=Hc) to (psi=v,X=X0,B=0)
and evaluates the Gibbs surface tension sigma(q).
"""
import argparse
import numpy as np
from scipy.integrate import solve_bvp, simpson


def vacuum(a,b,c):
    D=b-c*c
    v=np.sqrt(-(a+c)/(2*D))
    x0=np.sqrt((b+a*c)/D)
    return v,x0

def potential(f,x,a,b,c):
    return a*f*f+b*f**4+c*f*f*x*x-0.5*x*x+0.25*x**4

def solve_interface(q,a=-0.8,b=1.0,c=0.4,L=14.0,points=800,tol=1e-6,guess=None):
    v,x0=vacuum(a,b,c)
    Vmix=potential(v,x0,a,b,c)
    Vn=potential(0.0,1.0,a,b,c)
    Hc=np.sqrt(2*(Vn-Vmix))
    z=np.linspace(-L,L,points)
    if guess is None:
        s=0.5*(1+np.tanh(z/1.5))
        f=v*s
        x=1+(x0-1)*s
        A=Hc*(z-L)*(1-s)
        y=np.vstack([f,np.gradient(f,z),x,np.gradient(x,z),A,np.gradient(A,z)])
    else:
        y=guess.sol(z)
    def ode(zz,yy):
        f,fp,x,xp,A,Bf=yy
        return np.vstack([
            fp,
            q*q*A*A*f+(a+2*b*f*f+c*x*x)*f,
            xp,
            (-1+x*x+2*c*f*f)*x,
            Bf,
            2*q*q*f*f*A,
        ])
    def bc(ya,yb):
        return np.array([ya[0],ya[2]-1,ya[5]-Hc,yb[0]-v,yb[2]-x0,yb[4]])
    sol=solve_bvp(ode,bc,z,y,tol=tol,max_nodes=50000)
    if sol.status!=0:
        raise RuntimeError(sol.message)
    return sol,Hc,Vmix

def tension(q,**kwargs):
    L=kwargs.get('L',14.0)
    sol,Hc,Vmix=solve_interface(q,**kwargs)
    a=kwargs.get('a',-0.8); b=kwargs.get('b',1.0); c=kwargs.get('c',0.4)
    z=np.linspace(-L,L,24000)
    f,fp,x,xp,A,Bf=sol.sol(z)
    g=fp**2+q*q*A*A*f*f+0.5*xp**2+0.5*Bf**2+potential(f,x,a,b,c)-Hc*Bf
    return float(simpson(g-Vmix,x=z))

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--q',type=float,nargs='*',default=[1.28,1.2821745437,1.28275,1.2827788,1.283,1.285])
    args=p.parse_args()
    for q in args.q:
        print(f"{q:.10f},{tension(q):+.12e}")
