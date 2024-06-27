
16S amplicon is usual for taxa classification of eDNA projects.


## Data

Use [Silva - SSU](https://www.arb-silva.de/download/arb-files/) or [NCBI ftp -- cdhit](https://ftp.ncbi.nih.gov/blast/db/)

```bash
wget https://www.arb-silva.de/fileadmin/silva_databases/release_132/Exports/SILVA_132_SSURef_Nr99_tax_silva.fasta.gz
python split_data.py
cat Archaea.fa  Bacteria.fa > train.fa
# KMER=7
# jellyfish count -m $KMER -s 1G --bf-fp 0 -o jellyfish.$KMER.jf train.fa    ## Cannot Use, since there are degenerate symbols in .fa
# jellyfish dump jellyfish.$KMER.jf | grep -v '>' > jellyfish.$KMER.list

Archaea     25026    -->  10000   len: 1200~3100    Archaea.fa
Bacteria    592605   -->  10000   len: 1200~3100    Bacteria.fa
Eukaryota   77540
```

## Train

```bash
Input: Seq
Output: Predict Archaea(0) or Bacteria(1)
Model: Conv1d -- LSTM -- LinearClassifier

TODO: 
- Optimize the model
- Use blast result as benchmark.
```

 

