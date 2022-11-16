'''Deal with NA data points
'''

def drop(data, columns_l):
    '''Drop nas from a dataframe
    
    Args:
        data pd.DataFrame: input dataframe
        columns_l list: list of columns to be processed
    
    Return:
        proc_data pd.DataFrame: processed dataframe
    '''
    proc_data = data.dropna(subset=columns_l)

    return proc_data

def fill(data, columns_l):
    '''Fill nas from a dataframe
    
    Args:
        data pd.DataFrame: input dataframe
        columns_l list: list of columns to be processed
    
    Return:
        proc_data pd.DataFrame: processed dataframe
    '''
    print(data[columns_l].mean())
    proc_data = data.fillna(value=data[columns_l].mean())

    return proc_data
