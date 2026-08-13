"""Make v0.1 figures exclusively from campaign machine-readable output."""
from __future__ import annotations
import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def rows(path):
    with path.open(newline="") as f: return list(csv.DictReader(f))


def make_figures(root: Path) -> None:
    out=root/"figures"; out.mkdir(exist_ok=True)
    conv=rows(root/"convergence.csv")
    plt.figure(); plt.semilogy([int(x["initial_mesh_size"]) for x in conv],
        [float(x["residual_error_estimate"]) for x in conv],"o-")
    plt.xlabel("initial mesh size"); plt.ylabel("residual estimate"); plt.tight_layout(); plt.savefig(out/"convergence.png"); plt.close()
    giant=[x for x in rows(root/"giant_vortices.csv") if x["record_type"]=="root" and x["converged"]=="True"]
    n=[int(x["n"]) for x in giant]; q=[float(x["q"]) for x in giant]
    plt.figure(); plt.plot(n,q,"o-"); plt.xlabel("n"); plt.ylabel("q_c^(n)"); plt.tight_layout(); plt.savefig(out/"critical_roots.png"); plt.close()
    plt.figure(); plt.plot([1/x**.5 for x in n],[float(x["q_minus_qinf"]) for x in giant],"o")
    plt.xlabel("1/sqrt(n)"); plt.ylabel("q_c^(n)-q_inf"); plt.tight_layout(); plt.savefig(out/"large_n_residuals.png"); plt.close()
    interface=rows(root/"interface.csv"); plt.figure()
    plt.plot([float(x["q"]) for x in interface],[float(x["sigma"]) for x in interface],"o-"); plt.axhline(0,color="k",lw=.7)
    plt.xlabel("q"); plt.ylabel("sigma"); plt.tight_layout(); plt.savefig(out/"interface.png"); plt.close()
    plt.figure(); labels=[x["parameter_label"] for x in interface if x["record_type"]=="matching"]
    ai=[float(x["A_interface"]) for x in interface if x["record_type"]=="matching"]
    ad=[float(x["A_direct"]) for x in interface if x["record_type"]=="matching"]
    plt.plot(ai,ad,"o"); plt.xlabel("A_interface"); plt.ylabel("A_direct");
    for x,y,l in zip(ai,ad,labels): plt.annotate(l,(x,y))
    plt.tight_layout(); plt.savefig(out/"matching.png"); plt.close()
    pc=rows(root/"perturbative_C.csv"); plt.figure(); plt.plot([float(x["rho_X"]) for x in pc],[float(x["C_direct"]) for x in pc],"o-")
    plt.xlabel("rho_X"); plt.ylabel("C"); plt.tight_layout(); plt.savefig(out/"C_rho.png"); plt.close()
    ur=rows(root/"universal_response.csv"); plt.figure()
    for rho in sorted({x["rho_X"] for x in ur}):
        rr=[x for x in ur if x["rho_X"]==rho]; plt.plot([float(x["z"]) for x in rr],[float(x["F"]) for x in rr],label=f"rho={rho}")
    plt.xlabel("normalized coordinate"); plt.ylabel("F"); plt.legend(); plt.tight_layout(); plt.savefig(out/"universal_profiles.png"); plt.close()

