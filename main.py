import numpy as np 
from Tree import Tree
import pandas as pd 
from functions import entropy
from functions import informationGain

# inaro ham tagheer bede adresesho 
dfFeature = pd.read_csv('C:\\Users\\ASUS\\Desktop\\dsFinal\\Decision-Tree\\dataset\\feature_train.csv', nrows=10)
dfLabel = pd.read_csv('C:\\Users\\ASUS\\Desktop\\dsFinal\\Decision-Tree\\dataset\\label_train.csv', nrows=10)

data = dfFeature
label = dfLabel['Diabetes_012']

#tree = Tree()
#tree.createTree(data, label)

s = informationGain(data["Income"], label)
print(s)