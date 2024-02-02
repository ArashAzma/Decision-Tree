from Tree import Tree
from decisionTreeClassifier import decisionTreeClassifier
import pandas as pd 
import numpy as np 

dfFeature = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\feature_train.csv', nrows=500)
dfLabel = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\label_train.csv', nrows=500)

dfTest = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\feature_test.csv', nrows=3)

dataDF = pd.concat([dfFeature, dfLabel], axis=1)
dataDF = dataDF.drop_duplicates()

data = dataDF.drop('Diabetes_012', axis=1)
label = dataDF['Diabetes_012']

test = dfTest

print('training...')
dsc = decisionTreeClassifier(data, label)
print('done')

print('predictions', dsc.predictAll(test))