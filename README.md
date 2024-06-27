# BioDL
Some Trials


## Classifiers

* Classifying protein sequences to VFCID
    - Tips: we can initiallize the nn.Embedding layer with BLOSUM62 matrix

* Classifying 16S sequences to Archaea(0) or Bacteria(1)
    - Tips: embed nt with a vector of lengh 4, Conv1d to mimic the behaviors of kmers & also shorten the seq, LSTM because the seqs are of different length. 






