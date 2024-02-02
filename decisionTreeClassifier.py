from Tree import Tree

class decisionTreeClassifier:
    def __init__(self, data, labels, max_depth=10):
        self.max_depth = max_depth
        self.tree = Tree(depth=self.max_depth)
        self.decisionTree = self.tree.createTree(data, labels)

    def predict(self, data):
        predictedLabel = None
        root = self.tree.root

        while(predictedLabel == None):
            columnValue = data[root.featureName]      
            selectedNode = None
            
            for childRoot in root.children:
                if(childRoot.value == columnValue):
                    selectedNode = childRoot
                    break
            nodeType = selectedNode.whoami()

            if(nodeType == 'LeafNode'):
                predictedLabel = selectedNode.label
            elif(nodeType == 'Node'):
                root = selectedNode
        return predictedLabel

