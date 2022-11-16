'''Load the data
'''
import pandas as pd

def from_csv(filename):
    '''Reads data from csv

    Args:
        filename (str): filename and path of data
    
    Returns:
        data pd.DataFrame: data
    '''
    return pd.read_csv(filename, index_col=0)


