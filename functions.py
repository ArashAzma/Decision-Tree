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
        ent += (x / len(labels)) * np.log2(x / len(labels))
            
    return -ent  





def informationGain(labels, data):
    g = entropy(labels)
    dataTypes = []
    percents = []
    dataEntropy = []
    i = 0
    
    # finding data types
    for x in data :
        found = False
        for y in dataTypes :
            if(x == y) :
                found = True
                break
            else :
                i+=1
        if(not found) :
            dataTypes[i] = x
    ###
    
    #finding child entropies and number of each data type
    
    for x in range (0,len(dataTypes)-1) :
        datalabels = []
        for y in range (0, len (data) - 1):         # 0 ya 1 ro motmaen nistm (bastegi dare)
            if(data[y] == dataTypes[x]):
                percents[x] += 1
                datalabels.append(labels[y])
        dataEntropy[x] = entropy(datalabels)
    
    ###
        
    for x in range (0, len(dataTypes)-1) :
        g-=(percents[x]/len(labels))*dataEntropy[x]
    
    return g
