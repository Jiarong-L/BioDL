

Todo: Optimize the model


## Data

1. [Download](http://www.mgc.ac.cn/VFs/download.htm) VFDB protein sequences and remove redundancy

```bash
wget http://www.mgc.ac.cn/VFs/Down/VFDB_setA_pro.fas.gz
wget http://www.mgc.ac.cn/VFs/Down/VFDB_setB_pro.fas.gz
wget http://www.mgc.ac.cn/VFs/Down/VFs.xls.gz
less VFDB_setA_pro.fas.gz| grep '>' | wc -l    ## 4236 core dataset
less VFDB_setB_pro.fas.gz| grep '>' | wc -l    ## 27982 full dataset

cd-hit -i VFDB_setA_pro.fas.gz -o cdhit.VFDB_setA.faa  -c 1 -G 0 -aS 0.9  -d 0
cd-hit -i VFDB_setB_pro.fas.gz -o cdhit.VFDB_setB.faa  -c 1 -G 0 -aS 0.9  -d 0

cd-hit-2d -i VFDB_setA_pro.fas.gz -i2 VFDB_setB_pro.fas.gz -o cdhit.VFDB_setB.notinA.faa -c 0.99 -G 0 -aS 0.9  -d 0
```

2. Download proteins from Swiss-Prot, remove redundancy and remove VF seqs

```bash
wget https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz

cd-hit -i uniprot_sprot.fasta.gz -o cdhit.swiss.faa  -c 1 -G 0 -aS 0.9  -d 0
cd-hit-2d -i VFDB_setB_pro.fas.gz -i2 cdhit.swiss.faa -o cdhit.swiss.notinVFDB.faa -c 0.99 -G 0 -aS 0.9  -d 0

sed -e ':a;N;$!ba;s/\n/;/g' cdhit.swiss.notinVFDB.faa.clstr | sed -e "s/>Cluster/\n>Cluster/g" |less   ## clusters of VF
```

but perhaps there still will be VFs in swissport that is not recorded by VFDB...


## Task

```bash
Input seq, output VFCID or 'not VF'

 Testset:        cdhit.VFDB_setA.faa(4229)   &  xx% cdhit.swiss.notinVFDB.faa(476495)
Trainset: cdhit.VFDB_setB.notinA.faa(20301)  &  xx% cdhit.swiss.notinVFDB.faa(476495)
```

Split & Merge Data: Better to Randomize before pickup, but I'm just lazy
```bash
cat cdhit.VFDB_setB.notinA.faa > trainset.faa            ## 20301
head -180002 cdhit.swiss.notinVFDB.faa >> trainset.faa   ## 21211

cat cdhit.VFDB_setA.faa > testset.faa                    ## 4229              
tail -40001 cdhit.swiss.notinVFDB.faa >> testset.faa     ## 4631
```

