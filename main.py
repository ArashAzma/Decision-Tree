import numpy as np 
from Tree import Tree
import pandas as pd 
from functions import informationGain, entropy

# inaro ham tagheer bede adresesho 
dfFeature = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\feature_train.csv', nrows=5)
dfLabel = pd.read_csv('D:\\Downloads\\UNI 3\\Data Structure\\Decision Tree\\dataset\\label_train.csv', nrows=5)

data = dfFeature
label = dfLabel['Diabetes_012']
print('data', np.array(data["HighBP"]))
print('label', np.array(label))
#tree = Tree()
#tree.createTree(data, label)
s = informationGain(data["HighBP"], label)
print(s)