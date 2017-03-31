# Luc Pitre
# 30 March 2017
# creating functions for common methods in descriptive statistics

results = [22, 44, 3, 1, 6, 5, 9, 12, 28, 7]

def mean(dataset):
    sampleSize = len(dataset)
    sampleAdded = 0
    sampleMean = None
    for x in dataset:
        sampleAdded += x

    sampleMean = sampleAdded/sampleSize
    return sampleMean
    #end mean()

def median(dataset):
    print(dataset)
    #count the number of samples
    med = None
    sampleSize = len(dataset)
    #sort the numbers into ascending order
    dataset.sort()
    #working here:
    if sampleSize % 2 is 0:
        med = (dataset[int(sampleSize/2)]+dataset[int((sampleSize/2)+1)])/2
    elif sampleSize % 2 is 1:
        med = dataset[1]
    print(dataset)
    print(med)
    #find the one in the middle
    #end median()

print("mean : ", mean(results))
#median(results)
