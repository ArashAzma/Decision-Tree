class TNode:
    def __init__(self, data=0, labels=None, attribute=0, attribute_amount=0, right=None, left=None):
        self.data = data
        self.labels = labels if labels is not None else {}
        self.attribute = attribute
        self.attribute_amount = attribute_amount
        self.right = right
        self.left = left
