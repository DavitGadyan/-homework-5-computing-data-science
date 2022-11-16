'''Train a model
'''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


def train(model, X_train, y_train, X_features_l):
    '''Train a model

    Args:
        model str: model abbreviation
        X_train pandas.DataFrame: training set of features
        y_train pandas.Series: training set of target variable
        X_features_l list: features to be used in modeling
    
    Returns:
        trained_model sklearn.model: trained model from sklearn with weights
    '''
    # filter columns of train set
    X_train = X_train[X_features_l]

    # train model
    model_dict = {'rf': RandomForestClassifier(), 'lr': LogisticRegression()}
    trained_model = model_dict[model].fit(X_train, y_train)

    return trained_model

def predict(trained_model, X_train, y_train, X_test, y_test, X_features_l):
    '''Train a model

    Args:
        trained_model sklearn.model: trained model from sklearn with weights
        X_train pandas.DataFrame: training set of features
        y_train pandas.Series: training set of target variable
        X_test pandas.DataFrame: testing set of features
        y_test pandas.Series: testing set of target variable
        X_features_l list: features to be used in modeling
    
    Returns:
        y_train, y_test : train and test targets with predictions
    '''
    # filter columns of train set and test set
    X_train = X_train[X_features_l]
    X_test = X_test[X_features_l]

    # train model
    train_preds = trained_model.predict_proba(X_train)[:, 1]
    test_preds = trained_model.predict_proba(X_test)[:, 1]

    # make target series dataframes
    y_train = pd.DataFrame(y_train)
    y_test = pd.DataFrame(y_test)

    print('y_train>>>', y_train)
    print('y_test>>>', y_test)


    y_train['predictions'] = train_preds
    y_test['predictions'] = test_preds

    return y_train, y_test
