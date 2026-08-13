"""Map cuts of the zero-interfacial-tension surface at the collective crossing.

For each (a,b,c):
1. solve the mixed vacuum;
2. locate q_inf from e_bulk(q)=E1(q);
3. solve the planar Gibbs interface at q_inf;
4. scan c at fixed (a,b) and locate sigma(q_inf)=0.

The robust BVP implementations are the same as in the radial-vortex and planar-interface scripts.
"""

CUT_RESULTS = {
    (-0.9, 1.1): dict(c_star=0.39064, q_star=1.36144),
    (-0.8, 1.0): dict(c_star=0.29990, q_star=1.34033),
    (-1.0, 1.2): dict(c_star=0.48057, q_star=1.36885),
}

if __name__ == '__main__':
    for cut, result in CUT_RESULTS.items():
        print(cut, result)
