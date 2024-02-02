from Tree import Tree
import numpy as np
class decisionTreeClassifier:
    def __init__(self, data, labels, max_depth=10):
        self.max_depth = max_depth
        self.tree = Tree(depth=self.max_depth)
        self.decisionTree = self.tree.createTree(data, labels)

    def predictAll(self, data):
        dataArray = np.array(data)
        predictions = []
        i=0
        while i< len(dataArray):
            predictions.append(self.predict(data.iloc[i]))
            i+=1
        return predictions
        
    def predict(self, data):
        predictedLabel = None
        root = self.tree.root

        while(predictedLabel == None):
            if root.featureName == '':
                predictedLabel = 0
                continue
            columnValue = data[root.featureName]      
            selectedNode = None
            
            for childRoot in root.children:
                if(childRoot.value == columnValue):
                    selectedNode = childRoot
                    break
            if(selectedNode== None):
                predictedLabel = -1
                continue
            nodeType = selectedNode.whoami()

            if(nodeType == 'LeafNode'):
                predictedLabel = selectedNode.label
            elif(nodeType == 'Node'):
                root = selectedNode
        return predictedLabel

    def accuracy(self, predictedLabels, labels):
        i = 0
        correctPredictionCount = 0  
        while(i<len(labels)):
            if(predictedLabels[i] == labels[i]):
                correctPredictionCount+=1
            i+=1

        accuracy_value = correctPredictionCount/len(labels)

        return accuracy_value