from Tree import Tree
from decisionTreeClassifier import decisionTreeClassifier
import pandas as pd 
import numpy as np 

dfFeature = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\feature_train.csv', nrows=100)
dfLabel = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\label_train.csv', nrows=100)

# dfFeature = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\Iris.csv')

# data = dfFeature.drop("Id", axis=1)
# data = data.drop("Species", axis=1)
# label = dfFeature['Species']

data = dfFeature
label = dfLabel['Diabetes_012']


# tree = Tree(10)
# tree.createTree(data, label)
i = 0
while True:
    firstRow = data.iloc[i]
    dsc = decisionTreeClassifier(data, label)
    print(dsc.predict(firstRow))
    i+=1