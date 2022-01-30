"""Library of vizualization and plotting functions."""

import argparse as arg

import dtwf_lib as dtwf
import matplotlib.pyplot as plt
import moran_lib as mp

# Setting Matplotlib preferences
plt.rc("text", usetex=True)
plt.rc("font", family="serif")
plt.rc("figure", autolayout=True)


def plot_figure1(n, t, N, outfile, xlim=None):
    """Densities of lineages lost in one generation in Moran and DTWF models."""
    ymoran = mp.prob_lineages_step(n, t, N[0])
    ydtwf = dtwf.prob_anc(n, N[0])
    l_len = len(ymoran)
    ymoran = ymoran[1:l_len]
    ydtwf = ydtwf[1:l_len]
    x = [i for i in range(1, n + 1)]
    nl_moran = sum([i * ymoran[i] for i in range(n)])
    nl_dtwf = sum([i * ydtwf[i] for i in range(n)])
    print(f"E(NLFT | Moran) = {nl_moran}\nE(NLFT | DTWF) = {nl_dtwf}")
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(4, 2), sharey=True)
    ax1.bar(x, ymoran, linewidth=0, align="center")
    ax2.bar(x, ydtwf, linewidth=0, align="center")
    ax1.set_title("Moran Model")
    ax2.set_title("DTWF")
    ax1.set_ylabel(r"\textbf{Probability}")
    ax1.set_xlabel(r"\textit{m}")
    ax2.set_xlabel(r"\textit{m}")
    if xlim is not None:
        ax1.set_xlim(xlim)
        ax2.set_xlim(xlim)
    plt.tight_layout()
    plt.savefig(outfile, bbox_inches="tight", dpi=300)


# NOTE: should use pandas for this?
def read_nlft(filelist):
    """Read NLFT output files."""
    n_files = len(filelist)
    assert n_files > 0
    E_NLFT = []
    for i in range(0, n_files):
        cur_nlft = []
        with open(filelist[i]) as f:
            next(f)
            for line in f:
                e_nlft = float(line.split()[1])
                cur_nlft.append(e_nlft)
        E_NLFT.append(cur_nlft)
    return E_NLFT


def plot_figure2(outfile, moranfiles, coalfiles, legend):
    """Compare coalescent predictions to discrete Moran Model.

    Parameters:
        outfile - actual output eps/pdf/png file
        moranfiles - nlft output from moran.py
        coalfiles - nlft output from coalescent.py
        legend - labels to give legend (i.e. sample sizes)

    """
    assert len(moranfiles) == len(coalfiles)
    coal_exp = read_nlft(coalfiles)
    moran_exp = read_nlft(moranfiles)
    t = [i for i in range(1, len(coal_exp[0]) + 1)]
    for x in range(len(coal_exp)):
        cur_coal_exp = coal_exp[x]
        cur_moran_exp = moran_exp[x]
        cur_error = [
            (cur_moran_exp[i] - cur_coal_exp[i]) / cur_moran_exp[i] * 100.0
            for i in range(len(cur_moran_exp))
        ]
        plt.plot(t, cur_error)
    plt.legend(legend, loc="lower right")
    plt.xlabel(r"\textit{t}")
    plt.ylabel(r"$\frac{E[A_n^M(t)] - E[A_n^C(t)]}{E[A_n^M(t)]} \times 100\%$")
    plt.savefig(outfile, bbox_inches="tight", dpi=300)


def plot_figure3(outfile, moranfiles, dtwffiles, N, legend):
    """Compare the NLFT between DTWF and the Moran Model.

    Parameters:
        - outfile - the output png/pdf/eps file
        - moranfiles - list of moranfiles to read
        - dtwffiles - list of nlft files under the dtwf
        - N - constant population size (TODO : will change this soon)
        - legend - list of strings showing the legend

    """
    assert len(moranfiles) == len(dtwffiles)
    moran_exp = read_nlft(moranfiles)
    dtwf_exp = read_nlft(dtwffiles)
    t = [i for i in range(1, len(moran_exp[0]) + 1)]
    incr = int(N / 2)
    tot = int(len(t) / incr)
    t_dtwf = [i * incr for i in range(1, tot + 1)]
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))
    for j in range(len(dtwffiles)):
        cur_dtwf_exp = dtwf_exp[j]
        cur_moran_exp = moran_exp[j]
        error = []
        for i in range(0, len(cur_dtwf_exp)):
            print(
                "%d\t%d\t%0.8f\t%0.8f"
                % (
                    i,
                    incr + i * incr - 1,
                    cur_dtwf_exp[i],
                    cur_moran_exp[incr + i * incr - 1],
                )
            )
            cur_error = (
                cur_dtwf_exp[i] - cur_moran_exp[incr + i * incr - 1]
            ) / cur_dtwf_exp[i]
            error.append(cur_error * 100)
        ax.plot(t_dtwf, error)
    ax.set_ylim([min(error) - 0.5, max(error) + 0.5])
    ax.legend(legend, loc="lower right")
    ax.set_xlabel(r"\textit{t}")
    ax.set_ylabel(
        r"$\frac{E[A_n^D(t)] - E[A_n^M(t)]}{E[A_n^D(t)]} \times 100\%$"
    )  # noqa
    plt.tight_layout()
    ax.savefig(outfile, bbox_inches="tight", dpi=300)


def plot_figure4(outfile, moranfiles, dtwffiles, coalfiles, N, legend):
    """Plot nlft of dtwf and the moran model normalized by the coalescent rate."""
    assert len(moranfiles) == len(dtwffiles)
    assert len(dtwffiles) == len(coalfiles)
    moran_exp = read_nlft(moranfiles)
    dtwf_exp = read_nlft(dtwffiles)
    coal_exp = read_nlft(coalfiles)
    t = [i for i in range(1, len(moran_exp[0]) + 1)]
    incr = int(N / 2)
    tot = int(len(t) / incr)
    t_dtwf = [i * incr for i in range(1, tot + 1)]
    for j in range(len(coalfiles)):
        cur_dtwf_exp = dtwf_exp[j]
        cur_moran_exp = moran_exp[j]
        cur_coal_exp = coal_exp[j]
        dtwf_error = []
        moran_error = []
        for i in range(0, len(cur_dtwf_exp)):
            cur_dtwf_error = (
                (cur_dtwf_exp[i] - cur_coal_exp[incr + i * incr - 1]) / cur_dtwf_exp[i]
            )  # noqa
            cur_moran_error = (
                (cur_moran_exp[incr + i * incr - 1] - cur_coal_exp[incr + i * incr - 1])
                / cur_moran_exp[incr + i * incr - 1]
            )  # noqa
            dtwf_error.append(cur_dtwf_error * 100.0)
            moran_error.append(cur_moran_error * 100.0)
            print(f"{i}\t{cur_dtwf_error}\t{cur_moran_error}")
        plt.plot(t_dtwf, dtwf_error)
        plt.plot(t_dtwf, moran_error)
    plt.ylim([min(dtwf_error) - 0.01, 0.01])
    plt.legend(legend, loc="lower right")
    plt.xlabel(r"\textit{t}")
    plt.ylabel(r"Normalized Error $(\times 100\%)$")
    plt.savefig(outfile, bbox_inches="tight", dpi=300)


if __name__ == "__main__":
    # Parse all arguments
    parser = arg.ArgumentParser()
    parser.add_argument("-o", "--outfile", required=True, help="output figure file")
    parser.add_argument("-n", type=int, required=False, help="sample size", default=250)
    parser.add_argument(
        "-N", type=int, required=False, help="constant population size", default=20000
    )
    parser.add_argument(
        "-moranfiles",
        type=str,
        nargs="+",
        required=False,
        help="files detailing Moran NLFT",
    )
    parser.add_argument(
        "-coalfiles",
        type=str,
        nargs="+",
        required=False,
        help="files detailing Coalescent NLFT",
    )
    parser.add_argument(
        "-dtwffiles",
        type=str,
        nargs="+",
        required=False,
        help="files detailing NLFT for the Moran Model",
    )
    parser.add_argument(
        "-legend", type=str, nargs="+", required=False, help="legend labels for figure2"
    )
    parser.add_argument(
        "-figure1", action="store_true", required=False, help="Creating Figure 1"
    )
    parser.add_argument(
        "-figure2", action="store_true", required=False, help="Creating Figure 2"
    )
    parser.add_argument(
        "-figure3", action="store_true", required=False, help="Creating Figure 3"
    )
    parser.add_argument(
        "-figure4", action="store_true", required=False, help="Creating Figure 4"
    )
    args = parser.parse_args()

    # Going through all of the cases for figures
    if args.figure1:
        Ne = [args.N for i in range(int(1e6))]
        min_x = 0 if args.n - 30 < 0 else args.n - 30
        plot_figure1(args.n, args.N / 2, Ne, args.outfile, xlim=[min_x, args.n + 3])
    if args.figure2:
        print("Coalescent NLFT files : ", args.coalfiles)
        print("Moran NLFT files : ", args.moranfiles)
        plot_figure2(args.outfile, args.moranfiles, args.coalfiles, args.legend)
    if args.figure3:
        print("Moran NLFT files : ", args.moranfiles)
        print("DTWF NLFT files : ", args.dtwffiles)
        plot_figure3(args.outfile, args.moranfiles, args.dtwffiles, args.N, args.legend)
    if args.figure4:
        print("Moran NLFT files : ", args.moranfiles)
        print("DTWF NLFT files : ", args.dtwffiles)
        print("Coalescent NLFT files : ", args.coalfiles)
        plot_figure4(
            args.outfile,
            args.moranfiles,
            args.dtwffiles,
            args.coalfiles,
            args.N,
            args.legend,
        )
