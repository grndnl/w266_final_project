# On the effectiveness of Large Language Models in the mechanical design domain

Daniele Grandi, Fabian Riquelme

In this work, we seek to understand the performance of large language models in the mechanical engineering domain. We leverage the semantic data found in the ABC dataset, specifically the assembly names that designers assigned to the overall assemblies, and the individual semantic part names that were assigned to each part. After pre-processing the data we developed two unsupervised tasks to evaluate how different model architectures perform on domain-specific data: a binary sentence-pair classification task and a zero-shot classification task.  We achieved a 0.62 accuracy for the binary sentence-pair classification task with a fine-tuned model that focuses on fighting over-fitting: 1) modifying learning rates, 2) dropout values, 3) Sequence Length, and 4) adding a multi-head attention layer. Our model on the zero-shot classification task outperforms the baselines by a wide margin, and achieves a top-1 classification accuracy of 0.386. 
The results shed some light on the specific failure modes that arise when learning from language in this domain.

## Repository Structure
<pre>
.
├─ data                                     # Data folder and preprocessing code
│  ├─ extract_text_data.py                  # Takes the raw ABC data and extracts the `assembly names` and `part names`
│  ├─ clean_names.py                        # Takes the output of `extract_text_data.py` and peforms some cleaning and preprocessing steps, and EDA 
│  └─ Exploratory_analysis.ipynb            # EDA
|
├─ assembly_name_prediction           
│  ├─ assembly_name_prediction.ipnyb        # Notebook containing all relevant experiments for the assembly name prediction task
│  └─ fine_tuning                           # Code to perform language modeling pre-training using MLM method, copied from the <a href="https://github.com/huggingface/transformers/tree/main/examples/tensorflow/language-modeling">Huggingface repo</a> 
│ 
├─ sentence_pair_classification           
│  └─ sentence_pair_classification.ipnyb    # Notebook containing all relevant experiments for the sentence-pair binary classification task
│
└─ W266_Final_Project.pdf                   # Final paper


</pre>
