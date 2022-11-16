'''Calculate scores to evaluate models
'''
from sklearn.metrics import roc_auc_score

def roc_auc(y_true, y_preds):
    '''Calculate ROC AUC score

    Args:
        y_true pandas.Series: true target values
        y_preds pandas.Series: predicted target values
    
    Returns:
        roc_auc float: ROC AUC score
    '''
    roc_auc = roc_auc_score(y_true, y_preds)

    return roc_auc


