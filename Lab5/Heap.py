def buildMaxHeap(a):
    for i in range (len(a), -1, -1):
        a = maxHeapify(a, i)

def maxHeapify(a, i):
    root = i
    left = (2 * i) + 1
    right = (2 * i) + 2

    if ((left < len(a)) and (a[i] < a[left])):
        root = left
    
    if ((right < len(a)) and (a[i] < a[right])):
        root = right
    
    if (root != i):
        a[i],a[root] = a[root],a[i]
        maxHeapify(a, i)

def heapSort(a):
    a = buildMaxHeap(a)