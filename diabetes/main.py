from diabetes.data.load import from_csv
from diabetes.processing.train_test import split
from diabetes.processing.na import drop, fill
from diabetes.processing.dummy import generate, binarize
from diabetes.training.model import train, predict
from diabetes.evaluating.score import roc_auc

df = from_csv('data/sample_diabetes_mellitus_data.csv')

print(df)

df = drop(df, columns_l = ['age', 'gender', 'ethnicity'])

print('NaNs dropped in age, gender, ethnicity columns>>>>\n', df)

print(df.info())

df = fill(df, columns_l = ['height', 'weight'])
print('NaNs filled with means for height, weight columns>>>>\n', df.info())

df = generate(df, columns_l = ['ethnicity'])
print('NaNs filled with means for height, weight columns>>>>\n', df.info())

df = binarize(df, init_column_name='gender', binarized_column_name='M/F')
print('Binarized gender column to M/F>>>>\n', df.info())

X_train, X_test, y_train, y_test = split(data=df, target='diabetes_mellitus')

print(X_train)

trained_model = train(model='rf', X_train=X_train, y_train=y_train, X_features_l=['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis'])

print('trained_model>>', trained_model)

y_train, y_test = predict(trained_model, X_train, y_train, X_test, y_test, X_features_l=['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis'])

print('y_train>>>', y_train)
print('y_test>>>', y_test)

print('AUC ROC score Train: ', roc_auc(y_train['diabetes_mellitus'], y_train['predictions']))
print('AUC ROC score Test: ', roc_auc(y_test['diabetes_mellitus'], y_test['predictions']))