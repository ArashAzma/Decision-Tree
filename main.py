from Tree import Tree
import pandas as pd 


# inaro ham tagheer bede adresesho 
dfFeature = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\feature_train.csv', nrows=8)
dfLabel = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\label_train.csv', nrows=8)

data = dfFeature
label = dfLabel['Diabetes_012']
tree = Tree(10)
tree.createTree(data, label)