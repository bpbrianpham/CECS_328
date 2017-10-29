import statistics

def quickSearch(array, k):
    left = []
    right = []
    medianList = [array[0], array[(int)(len(array)/2)], array[len(array)-1]]
    pivot = statistics.median(medianList)
    if(pivot == array[0]): 
        array.remove(array[0])
    elif(pivot == array[(int)(len(array)/2)]): 
        array.remove(array[(int)(len(array)/2)])
    else:
        array.remove(array[len(array) - 1])
    
    for i in range(len(array)):
        if (array[i] <= pivot):
            left.append(array[i])
        else:
            right.append(array[i])

    if(k > (len(left) + 1)):
        return quickSearch(right, k - (len(left)+ 1))
    elif(k < (len(left) + 1)):
        return quickSearch(left, k)
    else:
        return pivot;