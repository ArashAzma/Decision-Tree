from Tree import Tree
import numpy as np
class decisionTreeClassifier:
    def __init__(self, data, labels):
        self.tree = Tree()
        self.decisionTree = self.tree.createTree(data, labels)

    def predictAll(self, data, depth=None):
        dataArray = np.array(data)
        predictions = []
        
        i=0
        while i< len(dataArray):
            predictions.append(self.predict(data.iloc[i], depth))
            i+=1
        return predictions
        
    def predict(self, data, depth=None):
        predictedLabel = None
        root = self.tree.root
        
        if depth is None:
            depth = self.tree.depth
        currentDepth = 0

        while(predictedLabel == None):

            if currentDepth == depth:
                if root.whoami() == 'LeafNode':
                    predictedLabel = root.label
                else :
                    predictedLabel = self.labelWithHighestPercentage(np.array(root.labels))
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

            currentDepth += 1

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
    
    def labelWithHighestPercentage(self, arr):
        count_dict = {}

        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        label = max(count_dict, key=count_dict.get)
        return label