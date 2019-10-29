
# Snakemake example

Simple text analysis using Snakemake.

## Goal

Take a given text in any language and find:

- Distribution of word lenghts
- Most common words
- Most common n-grams

## Preparation

You will need a Python 3.6 environment with installed Matplotlib and Snakemake. 
Either activate your existing environment and install Snakemake,
```
pip install snakemake
```

or create a new environment:
```
conda env create -f environment.yml --name sta
source activate sta
```


## Running the workflow

Dry run:
```
snakemake -n all
```

Plot rule graph (`graphviz` is needed):
```
snakemake --rulegraph all | dot -Tpdf > rulegraph.pdf
```

Plot DAG:
```
snakemake --dag all | dot -Tpdf > dag.pdf
```


Create specific file:
```
snakemake run/ngram-2.en.txt
```

Force re-execution of a rule:
```
snakemake -R plot run/results.pdf
```

Use multiple cores:
```
snakemake --cores 4 all
```
