import numpy as np 
from Tree import Tree
import pandas as pd 
from functions import entropy

# inaro ham tagheer bede adresesho 
dfFeature = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\feature_train.csv', nrows=10)
dfLabel = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\label_train.csv', nrows=10)

data = dfFeature
label = dfLabel['Diabetes_012']

tree = Tree()
tree.createTree(data, label)