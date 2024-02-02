from Tree import Tree
from decisionTreeClassifier import decisionTreeClassifier
import pandas as pd 
import numpy as np 
dfFeature = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\feature_train.csv')
dfLabel = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\label_train.csv')

dfTest = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\feature_test.csv')

dataDF = pd.concat([dfFeature, dfLabel], axis=1)
dfTestLabel = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\label_test.csv')
dataDF = dataDF.drop_duplicates()

data = dataDF.drop('Diabetes_012', axis=1)
label = dataDF['Diabetes_012']

test = dfTest

print('training...')
dsc = decisionTreeClassifier(data, label)
print('done')

predictions = dsc.predictAll(test)

accuracy = dsc.accuracy(predictions, np.array(dfTestLabel))

print('accuracy', accuracy)