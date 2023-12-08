## Student Info
B11902014 高浩鈞

# Stage-A Document Intelligence

## ReadMe!
```bash!
I have modified line 4 of streamlit-script.py under Anaconda3\envs\docint\Scripts
Original: 
from streamlit.cli import main
Modified:
from streamlit.**web.**cli import main
```

## Installation

```bash
conda create -n docint python=3.11
conda activate docint
conda install -c conda-forge ghostscript
pip install -r requirements.txt
----------------------------------------
Used: 
conda install -c conda-forge jieba
conda install -c conda-forge streamlit
conda install -c anaconda scikit-learn
----------------------------------------
May Used:
conda install -c conda-forge backports.tempfile 
```

## Flowchart
![BDS_HW3a flowchart](https://hackmd.io/_uploads/rkmD4hlLa.png)


## Target

An artificial intelligence that searches in which table in the given pdf file has the desired information.  

#### Input

1. pdf files with only tables inside
2. the searching keywords

#### Output

**the hole table with desired information in it**      

#### Run the System
streamlit run main.py    

#### Example

The given pdf file:  
![image](https://github.com/Stage-A/Document-Intelligence/blob/main/images/example1.png)
Search query:  

```commandline
非監督式學習的應用
```

Output:
![image](https://github.com/Stage-A/Document-Intelligence/blob/main/images/example2.png)

## How to contribute

* Every one finishes the whole project and pulls the requests , do not edit the main branch
* if your code is acceptable, we will add it into the main branch

## Note

* In hw3a, you can use any package you think would be helpful.
* It's also necessary to implement the UI.
* Also using draw io to draw a flow diagram is required.

## Background Knowledge

[Azure Document Intelligence]( https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence
)

## Test Document

[Document 1](https://docs.google.com/document/d/1Di5oVYhUF6p-zj2y0DEBBeTvhC91KhX8/edit?usp=sharing&ouid=107784913306655694785&rtpof=true&sd=true)
[Document 2](https://docs.google.com/document/d/1HiZrgIyvwY8Fi4eLS0QGUkkycngtD6XJ/edit?usp=sharing&ouid=107784913306655694785&rtpof=true&sd=true)
