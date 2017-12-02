import statistics

def quickSort(array):
    # if statement for base case
    if(len(array) <= 3):
        # swap = 0
        # while swap != 0:
        #     swap = 0    
        #     for i in range(len(array)):
        #         if(i+1 < len(array)):
        #             if(array[i] > array[i+1]):
        #                 array[i], array[i+1] = array[i+1], array[i]
        #                 swap = 1
        return insertionSort(array)
    else:
        left = []
        right = []
        medianList = [array[0], array[(int)(len(array)/2)], array[len(array)-1]]
        p = statistics.median(medianList)
        if(p == array[0]): 
            array.remove(array[0])
        elif(p == array[(int)(len(array)/2)]): 
            array.remove(array[(int)(len(array)/2)])
        else:
            array.remove(array[len(array) - 1])

        pivot = [p]
        
        for i in range(len(array)):
            if (array[i] <= pivot[0]):
                left.append(array[i])
            else:
                right.append(array[i])
        
        left = quickSort(left)
        right = quickSort(right)
        return (left + pivot + right)    



def insertionSort(array):
    for i in range (len(array)):
        for j in range (i, -1, -1):
            if(array[j] > array[i]):
                array[j], array[i] = array[i], array[j]
    return array
