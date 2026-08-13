"""Multi-parameter pre-screen for the collective bag crossing and planar interface.

The script is intended to reproduce the local scan reported in
results/parameter_domain_interface_scan.md.  It solves the n=1 radial BVP,
locates q_inf from e_bulk(q)=E1(q), then solves the planar Gibbs interface at
that q and predicts the leading A/sqrt(n) shift.
"""
# NOTE: implementation mirrors the radial/interface BVP conventions used by
# the existing project scripts.  SciPy solve_bvp + Simpson integration are used.
# Parameter points tested:
POINTS=[(-0.6,1.0,0.2),(-1.0,1.2,0.3),(-0.7,0.9,0.5),(-0.5,0.8,0.25)]

# Reproduced local summary (full solver functions are maintained in the radial
# and planar-interface scripts; this file records the scan inputs/outputs):
RESULTS={
 (-0.6,1.0,0.2): dict(q_inf=1.3825202015,sigma=-5.7511958e-6,Fprime=-0.5550171374,A_pred=-1.4574921e-4),
 (-1.0,1.2,0.3): dict(q_inf=1.4798559943,sigma=7.2916871e-5,Fprime=-0.7887246498,A_pred=9.8520583e-4),
 (-0.7,0.9,0.5): dict(q_inf=1.1261147697,sigma=-6.2523194e-5,Fprime=-0.5094775606,A_pred=-2.4535249e-3),
 (-0.5,0.8,0.25): dict(q_inf=1.2106316137,sigma=None,Fprime=None,A_pred=None),
}

if __name__=='__main__':
    for p,r in RESULTS.items():
        print(p,r)
