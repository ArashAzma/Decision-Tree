class Node:
    #feature node
    def __init__(self, data=0, labels=None, featureName="", value= -1):
        self.featureName = featureName
        self.value = value

        self.data = data
        self.labels = labels if labels is not None else {}
        
        self.children = []
        
        self.isFeature = True
    def whoami(self):
         return (type(self).__name__)
        
class LeafNode:
    #leaf node

    def __init__(self, value, label=None, labelLength=0):
        self.value = value
        
        self.label = label if label is not None else {}
        self.labelLength = labelLength
        
        self.isFeature = False

        self.isLeaf = True
    def whoami(self):
         return (type(self).__name__)
