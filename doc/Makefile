
moran_derivation:
		xelatex moran_derivation	
		bibtex moran_derivation
		xelatex moran_derivation
		xelatex moran_derivation

moran_figure1:
	python3 ../src/viz.py -figure1 -o ../plots/moran_figure1.eps

moran_figure2:
	python3 ../src/viz.py -figure1 -n 25 -N 200 -o ../plots/moran_figure2.eps

moran_figure3:
	python3 ../src/viz.py -figure2 -o ../plots/moran_figure3.eps -coalfiles ../data/moran_figure3/nlft_coal_20_1e6.txt ../data/moran_figure3/nlft_coal_200_1e6.txt ../data/moran_figure3/nlft_coal_2000_1e6.txt -moranfiles ../data/moran_figure3/nlft_moran_20_1e6.txt ../data/moran_figure3/nlft_moran_200_1e6.txt ../data/moran_figure3/nlft_moran_2000_1e6.txt -legend2 n=20 n=200 n=2000

moran_figure4:
	python3 ../src/viz.py -figure2 -moranfiles ../data/moran_figure4/nlft_moran_20_1e6.txt ../data/moran_figure4/nlft_moran_200_1e6.txt ../data/moran_figure4/nlft_moran_2000_1e6.txt -coalfiles ../data/moran_figure4/nlft_coal_20_1e6.txt ../data/moran_figure4/nlft_coal_200_1e6.txt ../data/moran_figure4/nlft_coal_2000_1e6.txt  -legend2 n=20 n=200 n=2000 -o ../plots/moran_figure4.eps

moran_figure5:
	python3 ../src/viz.py -figure3 -dtwffiles ../data/moran_figure5/nlft_dtwf_20_1e6gen.txt ../data/moran_figure5/nlft_dtwf_200_1e6gen.txt ../data/moran_figure5/nlft_dtwf_2000_1e6gen.txt -moranfiles ../data/moran_figure3/nlft_moran_20_1e6.txt  ../data/moran_figure3/nlft_moran_200_1e6.txt ../data/moran_figure3/nlft_moran_2000_1e6.txt -N 20000 -o ../plots/moran_figure5.eps -legend n=20 n=200 n=2000

dtwf_properties:
	xelatex dtwf_offspring
	xelatex dtwf_offspring

clean:
		rm -f *.log *.out *.aux *.pdf *.bak *.toc *.vrb *.nav *.snm *.bbl *.blg
