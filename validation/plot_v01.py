"""Make v0.1 figures exclusively from campaign machine-readable output."""
from __future__ import annotations
import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def rows(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def present(row, *keys):
    """True when all requested CSV fields contain numeric data.

    Failed solver records remain in the machine-readable CSVs with empty numeric
    fields.  Figures must not reinterpret those missing values as zero.
    """
    return all(row.get(k, "") not in ("", None) for k in keys)


def converged(row):
    return row.get("converged") == "True"


def make_figures(root: Path) -> None:
    out = root / "figures"
    out.mkdir(exist_ok=True)

    conv = [x for x in rows(root / "convergence.csv")
            if converged(x) and present(x, "initial_mesh_size", "residual_error_estimate")]
    plt.figure()
    plt.semilogy([int(x["initial_mesh_size"]) for x in conv],
                 [float(x["residual_error_estimate"]) for x in conv], "o-")
    plt.xlabel("initial mesh size")
    plt.ylabel("residual estimate")
    plt.tight_layout()
    plt.savefig(out / "convergence.png")
    plt.close()

    giant = [x for x in rows(root / "giant_vortices.csv")
             if x.get("record_type") == "root" and converged(x)
             and present(x, "n", "q", "q_minus_qinf")]
    n = [int(x["n"]) for x in giant]
    q = [float(x["q"]) for x in giant]
    plt.figure()
    plt.plot(n, q, "o-")
    plt.xlabel("n")
    plt.ylabel("q_c^(n)")
    plt.tight_layout()
    plt.savefig(out / "critical_roots.png")
    plt.close()

    plt.figure()
    plt.plot([1 / x**.5 for x in n],
             [float(x["q_minus_qinf"]) for x in giant], "o")
    plt.xlabel("1/sqrt(n)")
    plt.ylabel("q_c^(n)-q_inf")
    plt.tight_layout()
    plt.savefig(out / "large_n_residuals.png")
    plt.close()

    interface = rows(root / "interface.csv")
    interface_valid = [x for x in interface if converged(x) and present(x, "q", "sigma")]
    plt.figure()
    plt.plot([float(x["q"]) for x in interface_valid],
             [float(x["sigma"]) for x in interface_valid], "o-")
    plt.axhline(0, color="k", lw=.7)
    plt.xlabel("q")
    plt.ylabel("sigma")
    plt.tight_layout()
    plt.savefig(out / "interface.png")
    plt.close()

    matching = [x for x in interface
                if x.get("record_type") == "matching" and converged(x)
                and present(x, "A_interface", "A_direct")]
    plt.figure()
    labels = [x["parameter_label"] for x in matching]
    ai = [float(x["A_interface"]) for x in matching]
    ad = [float(x["A_direct"]) for x in matching]
    plt.plot(ai, ad, "o")
    plt.xlabel("A_interface")
    plt.ylabel("A_direct")
    for x, y, label in zip(ai, ad, labels):
        plt.annotate(label, (x, y))
    plt.tight_layout()
    plt.savefig(out / "matching.png")
    plt.close()

    pc = [x for x in rows(root / "perturbative_C.csv")
          if present(x, "rho_X", "C_direct")]
    plt.figure()
    plt.plot([float(x["rho_X"]) for x in pc],
             [float(x["C_direct"]) for x in pc], "o-")
    plt.xlabel("rho_X")
    plt.ylabel("C")
    plt.tight_layout()
    plt.savefig(out / "C_rho.png")
    plt.close()

    ur = [x for x in rows(root / "universal_response.csv")
          if converged(x) and present(x, "rho_X", "z", "F")]
    plt.figure()
    for rho in sorted({x["rho_X"] for x in ur}):
        rr = [x for x in ur if x["rho_X"] == rho]
        plt.plot([float(x["z"]) for x in rr],
                 [float(x["F"]) for x in rr], label=f"rho={rho}")
    plt.xlabel("normalized coordinate")
    plt.ylabel("F")
    if ur:
        plt.legend()
    plt.tight_layout()
    plt.savefig(out / "universal_profiles.png")
    plt.close()
