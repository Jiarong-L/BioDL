
Load .pdb structures as graph, Later for: Graph Embedding/...


## Dataset

Download Uniport Accession predicted by AlphaFold at [ftp site](https://ftp.ebi.ac.uk/pub/databases/alphafold/) 

```bash
## f4= AlphaFold_Accession  f5=version
wget https://ftp.ebi.ac.uk/pub/databases/alphafold/accession_ids.csv

cut -d ',' -f4 accession_ids.csv |while read dd ; do echo -e "wget https://alphafold.ebi.ac.uk/files/${dd}-model_v4.pdb"; done > download.sh
sh download.sh
```

AA Embedding: Download [BLOSUM62.txt](https://www.ncbi.nlm.nih.gov/IEB/ToolBox/C_DOC/lxr/source/data/BLOSUM62) and scale its eigen vector

Then turn .pdb to graph Using [Bio.PDB.PDBParser](https://biopython-cn.readthedocs.io/zh-cn/latest/cn/chr11.html) and [DGL](https://docs.dgl.ai/en/1.1.x/tutorials/blitz/)


Other Tips: [Graphein](https://graphein.ai/getting_started/installation.html) seems to be a good tool for loading smiles/pdbto graph. 


