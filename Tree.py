import TNode
import numpy as np

class Tree:
    depth : any
    root =TNode()    
    #def getDepth():
     #   return depth

    def Entropy(labels):
        ent = 0
        i = 0
        j = 0
        outputs : {}
        percents : {}

        for x in labels:
            found : False
            for y in outputs:
                j = 0
                if(y == x):
                    percents[j]+=1
                    j+=1
                    found = True
                    break
            if(found == False):
                outputs[i] = x
                percents[i] = 1
                i+=1

        for x in percents:
            ent+=((x/len(labels))*np.log2(x/len(labels)))
            
        return ent
    
    def iGain(EParent, WChildren,EChildren):
        g = 0
        i = 0
        
        for x in WChildren:
            g+=x*EChildren[i]
            i+=1

        g = EParent - g
        
        return g
    
    def best_split(data, labels):
        return split

    def createTree(root):
        
        if Entropy(root.labels) == 0 :
            return
        
        split = best_split(root.data, root.labels)
        rightNode = TNode()
        leftNode = TNode()
        root.right = rightNode
        root.left = leftNode
        
        root.attribute_amount = split.attribute_amount
        root.attribute = split.attribute
        root.labels = labels

        rightNode.data = split.less
        createTree(rightNode)
        
        leftNode.data = split.more
        createTree(leftNode)
        
        return

