from TNode import TNode
import numpy as np
from functions import entropy, informationGain


class Tree:
    # constructure
    def __init__(self, depth=None):
        self.depth = depth
        self.root = TNode()

    @staticmethod
    def Entropy(labels):
       return entropy(labels)
    
    @staticmethod
    def iGain(EParent, WChildren,EChildren):
        return informationGain(EParent, WChildren,EChildren)
    
    def best_split(self, data, labels):
        labelsArray = np.array(labels)

        # print(data)
        # print(labels, "\n")
        # print(labelsArray)

        feature = "Income"
        unique_values = data[feature].unique()
        for value in unique_values:
            subset_indices = data[feature] == value
            print(data[feature])
            print(subset_indices)
            # parentEntropy = self.Entropy(labelsArray)
            # weights_children = len(data[subset_indices]) / len(data)
            # childrenEntropy = self.Entropy(labels[subset_indices])
            # print(parentEntropy)
            # print(childrenEntropy)
        print("next value\n")
        # for feature in data.columns:
        #     unique_values = data[feature].unique()
        #     for value in unique_values:
        #         subset_indices = data[feature] == value
        #         parentEntropy = self.Entropy(labelsArray)
        #         weights_children = len(data[subset_indices]) / len(data)
        #         childrenEntropy = self.Entropy(labels[subset_indices])
        #         print(parentEntropy)
        #         print(childrenEntropy)
        #     print("next value\n")



    def createTree(self, data, label):
        # bebim mitoni ba label beri inja 
        if self.Entropy(root.labels) == 0 :
            return
        
        # man injori niaz daram
        split = self.best_split(data, label)
        
        rightNode = TNode()
        leftNode = TNode()
        root.right = rightNode
        root.left = leftNode
        
        root.attribute_amount = split.attribute_amount
        root.attribute = split.attribute
        root.labels = labels

        rightNode.data = split.less
        self.createTree(rightNode)
        
        leftNode.data = split.more
        self.createTree(leftNode)
        
        return


