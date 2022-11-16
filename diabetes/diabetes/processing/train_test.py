'''Split dataframe into train and test sets
'''
from sklearn.model_selection import train_test_split

def split(data, target):
    '''Split dataset into train and test sets

    Args:
        data pd.DataFrame: input raw dataframe
        target str: target column
    Returns:
        X_train, X_test, y_train, y_test 
    '''

    # define feature set X and traget variable y
    X, y = data.drop(columns=[target]), data[target]
    
    # divide into training and testing sets for features and target variables
    X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    return X_train, X_test, y_train, y_test

