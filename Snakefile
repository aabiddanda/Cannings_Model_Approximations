
rule all:
	input:
		'plots/figure1_n100_N10000.pdf',
		'plots/figure1_n1000_N10000.pdf',
		'plots/figure2.pdf',
		'plots/figure3.pdf',


rule build_libraries:
	output:
		'src/coalescent_lib.so',
		'src/moran_lib.so',
		'src/dtwf_lib.so'
	shell:
		"""
		cd src; make 
		"""

rule run_coal_nlft:
	"""Generates input formatted files."""
	input:
		coal_lib = 'src/coalescent_lib.so',
		coal_script = 'src/coalescent.py'
	output:
		'data/nlft/nlft_coal_{n}_{time}.txt'
	shell:
		"""
		python3 {input.coal_script} -n {wildcards.n} -N 10000 -t {wildcards.time} -nlft > {output}
		"""

rule run_moran_nlft:
	input:
		moran_lib = 'src/moran_lib.so',
		moran_script = 'src/moran.py'
	output:
		'data/nlft/nlft_moran_{n}_{time}.txt'
	shell:
		"""
		python3 {input.moran_script} -n {wildcards.n} -N 10000 -t {wildcards.time} -nlft > {output}
		"""

rule run_dtwf_nlft:
	input:
		moran_lib = 'src/dtwf_lib.so',
		moran_script = 'src/dtwf.py'
	output:
		'data/nlft/nlft_dtwf_{n}_{time}.txt'
	shell:
		"""
		python3 {input.moran_script} -n {wildcards.n} -N 10000 -t {wildcards.time} -nlft > {output}
		"""

rule moran_figure1:
	output:
		pdf = 'plots/figure1_n{n}_N{N}.pdf'
	shell:
		"""
		python3 src/viz.py -figure1 -n {wildcards.n} -N {wildcards.N} -o {output.pdf}
		"""

rule moran_figure2:
	input:
		coal_nlft = expand('data/nlft/nlft_coal_{n}_{time}.txt', n=[20,200,2000], time=10000),
		moran_nlft = expand('data/nlft/nlft_moran_{n}_{time}.txt', n=[20,200,2000], time=10000)
	output:
		pdf = 'plots/figure2.pdf'
	shell:
		"""
		python3 src/viz.py -figure2 -o {output.pdf} -coalfiles {input.coal_nlft} -moranfiles {input.moran_nlft} -legend n=20 n=200 n=2000
		"""

rule moran_figure3:
	input:
		moran_nlft = expand('data/nlft/nlft_moran_{n}_{time}.txt', n=[20,200,2000], time=10000),
		dtwf_nlft = expand('data/nlft/nlft_dtwf_{n}_{time}.txt', n=[20,200,2000], time=10000)
	output:
		pdf = 'plots/figure3.pdf'
	shell:
		"""
		python3 src/viz.py -figure3 -dtwffiles {input.dtwf_nlft} -moranfiles {input.moran_nlft} -N 10000 -o {output.pdf} -legend n=20 n=200 n=2000
		"""


# moran_figure6:
#   python3 ../src/viz.py -figure4 -dtwffiles ../data/moran_figure5/nlft_dtwf_2000_1e6gen.txt -moranfiles ../data/moran_figure3/nlft_moran_2000_1e6.txt -coalfiles ../data/moran_figure3/nlft_coal_2000_1e6.txt -N 20000 -o ../plots/moran_figure6.eps -legend DTWF Moran

