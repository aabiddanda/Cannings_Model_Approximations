
moran_derivation:
		xelatex moran_derivation	
		xelatex moran_derivation

moran_figure1:
	python3 ../src/viz.py -figure1 -o ../plots/moran_figure1.eps

moran_figure2:
	python3 ../src/viz.py -figure1 -n 25 -N 200 -o ../plots/moran_figure2.eps

moran_figure3:
	echo("Coming Soon!")

dtwf_properties:
	xelatex dtwf_offspring
	xelatex dtwf_offspring

clean:
		rm -f *.log *.out *.aux *.pdf *.bak *.toc *.vrb *.nav *.snm
