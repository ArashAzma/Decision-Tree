from Node import Node, LeafNode
import numpy as np
import pandas as pd
from functions import entropy, informationGain

class Tree:
    # constructure
    def __init__(self, depth=20):
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


    def createTree(self, data, label, root = None, current_depth=0):

        if root is None: 
            root = Node(data, label)
            self.root = root

        labelsArray = np.array(label)

        if self.Entropy(labelsArray) == 0 or current_depth == self.depth: 
            return

        bestSplitColumnName = self.best_split(data, label)
        uniqueValues = data[bestSplitColumnName].unique()
        
        root.featureName = bestSplitColumnName

        for value in uniqueValues:
            subset_indices = data[bestSplitColumnName] == value
            subsetArray = np.array(subset_indices)

            droppedColumnData = data.drop(bestSplitColumnName, axis = 1)
            
            dataArray = np.array(droppedColumnData)

            labelSubset = [labelsArray[i] for i, subIndex in enumerate(subsetArray) if subIndex]
            dataSubset = [dataArray[i] for i, subIndex in enumerate(subsetArray) if subIndex]


            if(self.isLeafNode(labelSubset)):
                node = LeafNode(value, labelSubset[0])
            
            else:
                node = Node(dataSubset, labelSubset, "", value)
                label_subset_df = pd.DataFrame({'label': labelSubset})
                data_subset_df = pd.DataFrame(dataSubset, columns=droppedColumnData.columns)
                self.createTree(data_subset_df, label_subset_df['label'], node, current_depth + 1)

            root.children.append(node)

    def isLeafNode(self, label):
        return self.Entropy(label) == 0

