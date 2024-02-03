from Tree import Tree
import turtle
from decisionTreeClassifier import decisionTreeClassifier
import pandas as pd 
import numpy as np 
dfFeature = pd.read_csv('C:\\Users\\ASUS\\Desktop\\dsFinal\\Decision-Tree\\dataset\\feature_train.csv', nrows=20)
dfLabel = pd.read_csv('C:\\Users\\ASUS\\Desktop\\dsFinal\\Decision-Tree\\dataset\\label_train.csv', nrows=20)

dfTest = pd.read_csv('C:\\Users\\ASUS\\Desktop\\dsFinal\\Decision-Tree\\dataset\\feature_test.csv')

dataDF = pd.concat([dfFeature, dfLabel], axis=1)
dfTestLabel = pd.read_csv('C:\\Users\\ASUS\\Desktop\\dsFinal\\Decision-Tree\\dataset\\label_test.csv')
dataDF = dataDF.drop_duplicates()

data = dataDF.drop('Diabetes_012', axis=1)
label = dataDF['Diabetes_012']

test = dfTest

print('training...')
dsc = decisionTreeClassifier(data, label)
print('done')

#predictions = dsc.predictAll(test)

#accuracy = dsc.accuracy(predictions, np.array(dfTestLabel))

#print('accuracy', accuracy)

screen = turtle.Screen()
screen.setup(2200, 700)
Tree.drawTree(dsc.tree.depth, dsc.tree.root,0, 250 , 40, 2200, 700)
