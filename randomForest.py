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

        for x in predictions:
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