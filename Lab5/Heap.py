def buildMaxHeap(a):
    n = len(a)
    for i in range (n, -1, -1):
        a = maxHeapify(a, i)
    

def maxHeapify(a, i):
    if a is not None:
        root = i
        left = (2 * i)
        right = (2 * i) + 1

        if ((left <= len(a)) and (a[i] < a[left])):
            root = left
        
        if ((right <= len(a)) and (a[i] < a[right])):
            root = right
        
        if (root != i):
            a[i],a[root] = a[root],a[i]
            maxHeapify(a, i)

def heapSort(a):
    a = buildMaxHeap(a)
    return a