from Tree import Tree
import turtle
from decisionTreeClassifier import decisionTreeClassifier
from randomForest import randomForest
import pandas as pd 
import numpy as np 


dfFeature = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\feature_train.csv', nrows=50)
dfLabel = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\label_train.csv', nrows=50)

dfTest = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\feature_test.csv')

dataDF = pd.concat([dfFeature, dfLabel], axis=1)

dfTestLabel = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\label_test.csv')

dataDF = dataDF.drop_duplicates()

data = dataDF.drop('Diabetes_012', axis=1)
label = dataDF['Diabetes_012']

test = dfTest

# print('training...')
# dsc = decisionTreeClassifier(data, label)
#print(label)

randTree = randomForest(20, dataDF)
randTree.predictRandomForest(test.iloc[1])


# print('done')

# predictions = dsc.predictAll(test)

# accuracy = dsc.accuracy(predictions, np.array(dfTestLabel))

# print('accuracy', accuracy)

# screen = turtle.Screen()
# screen.setup(2200, 700)
# outputs = []
# colors = ["pink", "red", "green", "blue", "yellow"]
# Tree.drawTree(dsc.tree.depth, dsc.tree.root,0, 250 , 40, 2200, 700, colors, outputs)
