# DescribeCtx
## Introduction
This is the implementation of DescribeCtx.
![](https://github.com/ICSE2021DescribeCtx/DescribeCtx/blob/master/overview.pdf)
## Requirements
* Java version: 1.8.0_181
* Python version: 3.7.2
* Tensorflow version: 1.15.0
* Dependencies: numpy, scikit-learn, networkx, pandas
## Usage
Fill directories following the comments in the code accordingly.
### Feature Extraction
* Call Graph: 
  * run APKCallGraph.java. It takes apps' apk files as input, and output the call graph of app and activity_id_mappings.
  * run get
* GUI Context: run get_activity_layout_text.py
* Permission Description: run extract_nlp.py and get_sim_perm.py
* Training and Prediction: run model.py
