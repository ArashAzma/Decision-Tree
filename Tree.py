import TNode
import numpy as np

class Tree:
    depth : any
    
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
            ent+=(x/len(labels))*np.log2(x/len(labels))
            
        return ent
    
    def iGain(EParent, WChildren,EChildren):
        g : any
        return g

    
