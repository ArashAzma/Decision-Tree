from Tree import Tree
import numpy as np
# from  decisionTreeClassifier import predict

class randomForest:
    def __init__(self, treeCount, dataset, samplePercentage = 0.15):            
        self.trees = []
        self.tree = Tree()
        self.samplePercentage = samplePercentage
        self.dataset = dataset
        self.treeCount = treeCount
        self.extractRandomDataAndLabelFromDataset()

    def extractRandomDataAndLabelFromDataset(self):
        sampleSize = int(self.dataset.shape[0] * self.samplePercentage)
        
        for i in range (0, self.treeCount):
            randomDataset = self.dataset.sample(sampleSize)
            randomData = randomDataset.drop('Diabetes_012', axis=1)
            randomLabels = randomDataset['Diabetes_012']
            
            randomTree = Tree()
            randomTree.createTree(randomData, randomLabels)
            self.trees.append(randomTree.root)

    def predict(self, data, depth=None, root=None):
        predictedLabel = None
    
        if root is None:
            return 0

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
                predictedLabel = 0
                continue

            nodeType = selectedNode.whoami()

            if(nodeType == 'LeafNode'):
                predictedLabel = selectedNode.label

            elif(nodeType == 'Node'):
                root = selectedNode

            currentDepth += 1

        return predictedLabel

    def predictRandomForest (self, data, depth=4) :
        predictions = []
        for root in self.trees:
            if(root.featureName==""): continue
            prediction = self.predict(data, depth, root)
            predictions.append(prediction)
        outputs = []
        percents = []
        max = 0

        for i in range (0, len(predictions)) :
            found = False
            j = 0
            for i in range (0, len(outputs)) :
                if predictions[i] == outputs[j] :
                    percents[j] += 1
                    found = True
                    break
                j += 1
            if not found:
                outputs.append(predictions[i])
                percents.append(1)
                i += 1

        
        for x in range (0, len(percents) - 1) :
            if percents[x] > percents[max] :
                max = x
        
        return outputs[max]
    
    def predictAll(self, data, depth=None):
        dataArray = np.array(data)
        predictions = []
        
        i=0
        while i< len(dataArray):
            predictions.append(self.predictRandomForest(data.iloc[i], depth))
            i+=1
        return predictions
    
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
    