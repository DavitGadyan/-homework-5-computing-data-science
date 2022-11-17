'''Dummify data points
'''
import pandas as pd

def generate(data, columns_l):
    '''Generate dummies from a dataframe
    
    Args:
        data pd.DataFrame: input dataframe
        columns_l list: list of columns to be processed
    
    Return:
        proc_data pd.DataFrame: processed dataframe
    '''
    try:
        proc_data = pd.get_dummies(data=data, columns=columns_l)
        return proc_data

    except KeyError:
        raise Exception ('Please make sure columns exist in your data!!')

def binarize(data, init_column_name, binarized_column_name):
    '''Generate binary variable for gender
    
    Args:
        data pd.DataFrame: input dataframe
        init_column_name str: initial name of gender column
        binarized_column_name str: binarized name of gender column
    
    Return:
        proc_data pd.DataFrame: processed dataframe
    '''
    try:
        proc_data = pd.get_dummies(data=data, columns=[init_column_name], drop_first=True)
        proc_data = proc_data.rename(columns={[col for col in proc_data.columns if f'{init_column_name}_' in col][0]: binarized_column_name})
        return proc_data
    except KeyError:
        raise Exception ('Please make sure columns exist in your data!!')       
