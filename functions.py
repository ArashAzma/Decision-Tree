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






def informationGain(data, labels):
    dataTypes = data.unique()

    # data frames to 1d array
    dataArray = np.array(data)
    labelsArray = np.array(labels)

    g = entropy(labelsArray)
    dataTypes = []
    percents = []
    dataEntropy = []
    i = 0
    
    #finding child entropies and number of each data type
    
    for x in range (0,len(dataTypes)-1) :
        datalabels = []
        for y in range (0, len (dataArray) - 1):         # 0 ya 1 ro motmaen nistm (bastegi dare)
            if(dataArray[y] == dataTypes[x]):
                percents[x] += 1
                datalabels.append(labelsArray[y])
        dataEntropy[x] = entropy(datalabels)
    
    ###
        
    for x in range (0, len(dataTypes)-1) :
        g-=(percents[x]/len(labelsArray))*dataEntropy[x]
    
    return g
