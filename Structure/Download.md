
Load structures as graph, Later for GNN tasks [GNN_PyTorch.ipynb](https://github.com/Jiarong-L/GAN_tutorial/blob/main/Basis/GNN_PyTorch.ipynb)


## CBSI -- SMILES

Microtubule-targeted agents (Taxane, Vinblastine, CBSIs) may prevent the proliferation of tumor cells. Within which CBSIs are much easier to be modified.

Download from [ChEMBL](https://www.ebi.ac.uk/chembl/): Search for "Tubulin" -- Target (protein/chain) -- Homo sapiens -- Pick the target you want -- Activity Charts -- Associated Bioactivities -- Activity Types for ... -- Select All & Export CSV -- Then get Molecules ID and their records (.smiles/IC50/Activity/Kd/..)


## .pdb

Download Uniport Accession predicted by AlphaFold at [ftp site](https://ftp.ebi.ac.uk/pub/databases/alphafold/) 

```bash
## f4= AlphaFold_Accession  f5=version
wget https://ftp.ebi.ac.uk/pub/databases/alphafold/accession_ids.csv

cut -d ',' -f4 accession_ids.csv |while read dd ; do echo -e "wget https://alphafold.ebi.ac.uk/files/${dd}-model_v4.pdb"; done > download.sh
sh download.sh
```

AA Embedding: Download [BLOSUM62.txt](https://www.ncbi.nlm.nih.gov/IEB/ToolBox/C_DOC/lxr/source/data/BLOSUM62) and scale its eigen vector

Then turn .pdb to graph Using [Bio.PDB.PDBParser](https://biopython-cn.readthedocs.io/zh-cn/latest/cn/chr11.html) and [DGL](https://docs.dgl.ai/en/1.1.x/tutorials/blitz/)


Other Tips: [Graphein](https://graphein.ai/getting_started/installation.html) seems to be a good tool for loading smiles/pdb to graph. 



