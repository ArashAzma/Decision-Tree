from Tree import Tree
import numpy as np
from  decisionTreeClassifier import predict

class randomForest:
    def __init__(self, data, labels, num):            #num:tedade derakhtha
        self.trees = []
        self.tree = Tree()

        for i in range (0, num-1):
            self.trees.append(self.tree.createTree(randomData, randomLabels))   

    def predict (self, data) :
        predicts = []
        for i in range (0, len(self.trees)-1) :
            predicts.append(predict(self, data, depth=None))

        outputs = []
        percents = []
        max = 0

        for x in predicts:
            found = False
            j = 0
            for y in outputs:
                if y == x:
                    percents[j] += 1
                    found = True
                    break
                j += 1
            if not found:
                outputs.append(x)
                percents.append(1)
                i += 1

        
        for x in range (0, len(percents) - 1) :
            if percents[x] > percents[max] :
                max = x
        
        return outputs[max]