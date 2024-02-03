from Tree import Tree
import turtle
from decisionTreeClassifier import decisionTreeClassifier
from randomForest import randomForest
import pandas as pd 
import numpy as np 


dfFeature = pd.read_csv('C:\\Users\\ASUS\\Desktop\\dsFinal\\Decision-Tree\\dataset\\feature_train.csv', nrows=50)
dfLabel = pd.read_csv('C:\\Users\\ASUS\\Desktop\\dsFinal\\Decision-Tree\\dataset\\label_train.csv', nrows=50)

dfTest = pd.read_csv('C:\\Users\\ASUS\\Desktop\\dsFinal\\Decision-Tree\\dataset\\feature_test.csv')

dataDF = pd.concat([dfFeature, dfLabel], axis=1)

dfTestLabel = pd.read_csv('C:\\Users\\ASUS\\Desktop\\dsFinal\\Decision-Tree\\dataset\\label_test.csv')

dataDF = dataDF.drop_duplicates()

data = dataDF.drop('Diabetes_012', axis=1)
label = dataDF['Diabetes_012']

test = dfTest

print('training...')
dsc = decisionTreeClassifier(data, label)
randTree = randomForest(20, dataDF)
print('done')

predictions = randTree.predictAll(test)
print('random forest', randTree.accuracy(predictions, np.array(dfTestLabel)))

predictions2 = dsc.predictAll(test)
accuracy2 = dsc.accuracy(predictions2, np.array(dfTestLabel))
print('decision tree', accuracy2)



# screen = turtle.Screen()
# screen.setup(2200, 700)
# outputs = []
# colors = ["pink", "red", "green", "blue", "yellow"]
# Tree.drawTree(dsc.tree.depth, dsc.tree.root,0, 250 , 40, 2200, 700, colors, outputs)
