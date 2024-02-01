class Node:
    #feature node
    def __init__(self, data=0, labels=None, featureName="", value= -1):
        self.featureName = featureName
        self.value = value

        self.data = data
        self.labels = labels if labels is not None else {}
        
        self.children = []
        
        self.isFeature = True
    
        
class LeafNode:
    #leaf node
    def __init__(self, label=None, value= -1):
        self.value = value
        
        self.label = label if label is not None else {}
        
        self.isLeaf = True
