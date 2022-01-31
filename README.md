# Cannings-Models Approximation

This repository contains initial experiments exploring the implications of the discrete time wright-fisher (DTWF) model and the Moran model and their asymptotic properties in the limit of large sample-sizes relative to the population sizes (n > sqrt(N))

A large part of this was inspired by the influential paper by Bhaskar,Clark, and Song.

## Requirements

All of the requirements are spectified in `requirements.txt` and can be installed via:

```bash
pip3 install -r requirements.txt
```

## Regenerating Plots

In order to regenerate the various plots, we have provided a `snakemake` file that allows for regeneration of all of the various plots. To run the top-level simulations (they take ~15 minutes on a 2020 Macbook Air), run:

```
snakemake -j4 -p -n
```

, and remove the `-n` when actually running the pipeline.

## Regenerating Report

To regenerate the LaTeX-based report, you can simply head into the `doc/` directory and run `make`, which should build the current report.

# References

- [Bhaskar, Clark, and Song](https://doi.org/10.1073/pnas.1322709111)
- [snakemake](https://snakemake.readthedocs.io/en/stable/)
