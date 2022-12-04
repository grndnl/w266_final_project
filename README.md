# w266 Final Project

Daniele Grandi

Fabian Riquelme

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
