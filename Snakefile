#!python3


rule all:
    input:
        "plots/figure1_n250_N20000.pdf",
        "plots/figure1_n50_N200.pdf",
        # "plots/figure2.pdf",
        "plots/figure2a.pdf",
        "plots/figure3.pdf",
        "plots/figure4.pdf",


rule build_libraries:
    output:
        "src/coalescent_lib.so",
        "src/moran_lib.so",
        "src/dtwf_lib.so",
    shell:
        """
        cd src/; make
        """


rule run_coal_nlft:
    """Generates input formatted files."""
    input:
        coal_lib="src/coalescent_lib.so",
        coal_script="src/coalescent.py",
    output:
        "data/nlft/nlft_coal_n{n}_N{N}_{time}.txt.gz",
    shell:
        """
        python3 {input.coal_script} -n {wildcards.n} -N {wildcards.N} -t {wildcards.time} -nlft | gzip > {output}
        """


rule run_moran_nlft:
    input:
        moran_lib="src/moran_lib.so",
        moran_script="src/moran.py",
    output:
        "data/nlft/nlft_moran_n{n}_N{N}_{time}.txt.gz",
    shell:
        """
        python3 {input.moran_script} -n {wildcards.n} -N {wildcards.N} -t {wildcards.time} -nlft | gzip > {output}
        """


rule run_dtwf_nlft:
    input:
        dtwf_lib="src/dtwf_lib.so",
        dtwf_script="src/dtwf.py",
    output:
        "data/nlft/nlft_dtwf_n{n}_N{N}_{time}.txt.gz",
    shell:
        """
        python3 {input.dtwf_script} -n {wildcards.n} -N {wildcards.N} -t {wildcards.time} -nlft | gzip > {output}
        """


rule moran_figure1:
    input:
        rules.build_libraries.output,
    output:
        pdf="plots/figure1_n{n}_N{N}.pdf",
    shell:
        """
        python3 src/viz.py -figure1 -n {wildcards.n} -N {wildcards.N} -o {output.pdf}
        """


rule moran_figure2:
    input:
        coal_nlft=expand(
            "data/nlft/nlft_coal_n{n}_N{N}_{time}.txt.gz",
            N=20000,
            n=[20, 200, 2000],
            time=1000000,
        ),
        moran_nlft=expand(
            "data/nlft/nlft_moran_n{n}_N{N}_{time}.txt.gz",
            N=20000,
            n=[20, 200, 2000],
            time=1000000,
        ),
        libraries=rules.build_libraries.output,
    output:
        pdf="plots/figure2.pdf",
    shell:
        """
        python3 src/viz.py -figure2 -o {output.pdf} -coalfiles {input.coal_nlft} -moranfiles {input.moran_nlft} -legend n=20 n=200 n=2000
        """


rule moran_figure2a:
    input:
        coal_nlft=expand(
            "data/nlft/nlft_coal_n{n}_N{N}_{time}.txt.gz",
            N=2000,
            n=[20, 200, 2000],
            time=1000000,
        ),
        moran_nlft=expand(
            "data/nlft/nlft_moran_n{n}_N{N}_{time}.txt.gz",
            N=2000,
            n=[20, 200, 2000],
            time=1000000,
        ),
        libraries=rules.build_libraries.output,
    output:
        pdf="plots/figure2a.pdf",
    shell:
        """
        python3 src/viz.py -figure2 -o {output.pdf} -coalfiles {input.coal_nlft} -moranfiles {input.moran_nlft} -legend n=20 n=200 n=2000
        """


rule moran_figure3:
    input:
        moran_nlft=expand(
            "data/nlft/nlft_moran_n{n}_N{N}_{time}.txt.gz",
            n=[20, 200],
            N=10000,
            time=10000,
        ),
        dtwf_nlft=expand(
            "data/nlft/nlft_dtwf_n{n}_N{N}_{time}.txt.gz",
            n=[20, 200],
            N=10000,
            time=10000,
        ),
        libraries=rules.build_libraries.output,
    output:
        pdf="plots/figure3.pdf",
    shell:
        """
        python3 src/viz.py -figure3 -dtwffiles {input.dtwf_nlft} -moranfiles {input.moran_nlft} -N 10000 -o {output.pdf} -legend n=20 n=200
        """


rule moran_figure4:
    input:
        dtwf_nlft=expand(
            "data/nlft/nlft_dtwf_n{n}_N{N}_{time}.txt.gz", n=200, N=10000, time=1000000
        ),
        moran_nlft=expand(
            "data/nlft/nlft_moran_n{n}_N{N}_{time}.txt.gz",
            n=200,
            N=10000,
            time=1000000,
        ),
        coal_nlft=expand(
            "data/nlft/nlft_coal_n{n}_N{N}_{time}.txt.gz", n=200, N=10000, time=1000000
        ),
        libraries=rules.build_libraries.output,
    output:
        pdf="plots/figure4.pdf",
    shell:
        """
        python3 src/viz.py -figure4 -dtwffiles {input.dtwf_nlft} -moranfiles {input.moran_nlft} -coalfiles {input.coal_nlft} -N 10000 -legend DTWF Moran Coalescent -o {output.pdf}
        """
