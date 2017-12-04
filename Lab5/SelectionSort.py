def selectionSort(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i + 1, len(array)):
            if (array[j] < array[i]): 
                minimum = j
        array[minimum], array[i] = array[i], array[minimum]
    return array        