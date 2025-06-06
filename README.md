# BioDL

Toys that help to learn tools and methods, using PyTorch or TensorFlow or [Jax](https://jiarong-l.github.io/notes/Tricks/Jax/).

-	Generative models using MNIST images
-	Load and embed biological inputs (seq/structure) 
-	[Model explanation](https://jiarong-l.github.io/notes/Readings/XAI/) using Captum/SHAP 
-	Deploy model on [HuggingFace](https://jiarong-l.github.io/notes/Tricks/HuggingFace/)


## Trials

1. Classifying protein sequences to VFCID
    - Tips: we can initiallize the nn.Embedding layer with BLOSUM62 matrix

2. Classifying 16S RNA sequences to Archaea(0) or Bacteria(1)
    - Tips: embed nt with a vector of lengh 4, Conv1d to mimic the behaviors of kmers & also shorten the seq, do LSTM because the seqs are of different length. 

3. Load Structure data into Graph

4. Play around with protein profile with TimeLine info
    - AE: add constrains to preserve certain information in the emdeddings
    - AutoGluon: AutoML for table data



## Pending

* Community: A toy simulation try to recover community abundances from metagenomics data

