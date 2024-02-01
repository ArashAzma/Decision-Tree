import numpy as np

def entropy(labels):
    ent = 0
    i = 0
    j = 0
    outputs = []
    percents = []

    for x in labels:
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

    for x in percents:
        px = x / len(labels)
        ent += px * np.log2(px)
            
    return -ent  

def informationGain(EParent, WChildren,EChildren):
    g = 0
    i = 0
    
    for x in WChildren:
        g+=x*EChildren[i]
        i+=1

    g = EParent - g
    
    return g