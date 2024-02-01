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
    uniqueValues = data.unique()

    # data frames to 1d array
    dataArray = np.array(data)
    labelsArray = np.array(labels)

    parentEntropy = entropy(labelsArray)
    percents = np.zeros(len(uniqueValues))
    dataEntropy = np.zeros(len(uniqueValues))
    
    #finding child entropies and number of each data type
    for index, value in enumerate(uniqueValues):
        subset_indices = data == value
        subsetArray = np.array(subset_indices)
        trueCount = np.sum(subsetArray)
        percents[index] = trueCount/len(subsetArray)
        
        datalabels = [labelsArray[i] for i, subIndex in enumerate(subsetArray) if subIndex]
        dataEntropy[index] = entropy(datalabels)
    
    print('parentEntropy', parentEntropy)
    print('percents', percents)
    print('dataEntropy', dataEntropy)
    gain = parentEntropy
    for x in uniqueValues :
        gain-=(percents[x]/len(labelsArray)) * dataEntropy[x]
    
    return gain
