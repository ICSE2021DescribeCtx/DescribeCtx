# DescribeCtx
## Introduction
This is the implementation of DescribeCtx. Our works aims at synthesizing precise descriptions for sensitive behaviors in Android apps. DescribeCtx contains two phases: (1) training phase, and (2) prediction phase.

During the training phase, DescribeCtx first extracts both source-code-level and GUI-level contextual text from apk files of Android apps, additionally, DescribeCtx also extract permission descriptions from apps' privacy policy. These information is formally encoded and passed to a seq2seq-based language model to synthesize sensitive behavior descriptions.

During the prediction phase, given an app's GUI context and sensitive API call graph, DescribeCtx using the most similar permission description from other apps, to synthesize the description for the given sensitive behavior.
![](https://github.com/ICSE2021DescribeCtx/DescribeCtx/blob/master/overview1.jpg)
## Requirements
* Java version: 1.8.0_181
* Python version: 3.7.2
* Tensorflow version: 1.15.0
* Dependencies: numpy, scikit-learn, networkx, pandas
## Usage
Fill directories following the comments in the code accordingly.
### Feature Extraction
* Call Graph: 
  * run APKCallGraph.java. It takes apps' apk files as input, and output the call graph of app and activity_id_mappings. You can either hard code the apks and their paths in the program after you import to an IDE (such as Intellij), or you can make a jar file and pass the parameters through command line.
  * run getsubcg.py. It takes apps' dot files (call graphs) as input, and output the subgraph of sensitive API calls.
* GUI Context: run get_activity_layout_text.py. It takes activity_id_mappings and subgraph as input, and output the sensitive behavior related GUI context
* Permission Description: run extract_nlp.py. It takes raw privacy policy of each app as input, output the sensitive permission description sentences.
### Training and Prediction
* run model.py. The model takes triples (<permission description, call graph, GUI context>) as input data. The dataset has been splitted, after the training session is done, the program shows the synthesized description for testing samples.
