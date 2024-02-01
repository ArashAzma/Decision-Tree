from Node import Node, LeafNode
import numpy as np
import pandas as pd
from functions import entropy, informationGain


class Tree:
    # constructure
    def __init__(self, depth=None):
        self.depth = depth
        self.root = Node()

    @staticmethod
    def Entropy(labels):
       return entropy(labels)
    
    @staticmethod
    def iGain(data, labels):
        return informationGain(data, labels)
    
    def best_split(self, data, labels):
        best_feature_name = None
        best_gain = -1

        for feature in data.columns:
            gain = self.iGain(data[feature], labels)

            if gain > best_gain:
                best_gain = gain
                best_feature_name = feature

        return best_feature_name


    def createTree(self, data, label, root = None):

        if root is None: 
            root = self.root

        labelsArray = np.array(label)
        print(self.Entropy(labelsArray))
        if self.Entropy(labelsArray) == 0: 
            return

        bestSplitColumnName = self.best_split(data, label)
        print('bestSplitColumnName', bestSplitColumnName)
        uniqueValues = data[bestSplitColumnName].unique()

        for value in uniqueValues:
            subset_indices = data[bestSplitColumnName] == value
            subsetArray = np.array(subset_indices)

            droppedColumnData = data.drop(bestSplitColumnName, axis = 1)
            
            dataArray = np.array(droppedColumnData)

            labelSubset = [labelsArray[i] for i, subIndex in enumerate(subsetArray) if subIndex]
            dataSubset = [dataArray[i] for i, subIndex in enumerate(subsetArray) if subIndex]

            if(self.isLeafNode(labelSubset)):
                node = LeafNode(labelSubset[0], value)
                root.children.append(node)
            
            else:
                node = Node(dataSubset, labelSubset, bestSplitColumnName, value)
                label_subset_df = pd.DataFrame({'label': labelSubset})
                data_subset_df = pd.DataFrame(dataSubset, columns=droppedColumnData.columns)
                self.createTree(data_subset_df, label_subset_df['label'], node)

    def isLeafNode(self, label):
        return self.Entropy(label) == 0

