# homework-5-computing-data-science

### hw5.py
Python file with solution for each task

### diabetes_analysis python package 

#### folder structure

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   │
│   └── sample_diabetes_mellitus_data.csv            <- Input datadump.
│
│
├── notebooks          <- Jupyter notebooks testing the diabetes package (hm5_testing.ipynb)
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           
│   │   │
│   │   └── load.py    <- Read data
│   │
│   │
│   ├── processing     <- Scripts to process data (remove nas, dummify, split into train andt test)
│   │   │ 
│   │   ├── dummy.py   <- Scripts to dummify 
│   │   ├── na.py      <- Scripts to deal with nas 
│   │   └── train_test.py <- Scripts to divide data into train and test sets
│   │
│   ├── evaluating     <- Scripts to evaluate model 
│   │   │ 
│   │   └── score.py   <- Scripts to evaluate train test set using roc auc
│   │
│   └── training       <- Scripts to train model
│       └── model.py   <- Scripts to train model
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```
