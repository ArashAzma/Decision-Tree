import numpy as np

#def entropy(px):
#    return -np.sum(px * np.log2(px))

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
        ent += (x / len(labels)) * np.log2(x / len(labels))
            
    return -ent  
