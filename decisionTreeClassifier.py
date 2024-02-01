from Node import Node, LeafNode
from Tree import Tree

class decisionTreeClassifier:
    def __init__(self, data, labels, max_depth=10):
        self.max_depth = max_depth
        self.tree = Tree(depth=self.max_depth)
        self.decisionTree = self.tree.createTree(data, labels)

    def predict(self, data):
        print('self.tree.root.children', self.tree.root.children)
        print('self.tree.root.children', self.tree.root.children[0].label)
        print('self.tree.root.featureName', self.tree.root.featureName)
        # print(self.tree.root)
        # Implement prediction logic using the trained tree
        pass