def buildMaxHeap(array):
    for i in range(len(array)-1, -1, -1):
        maxHeapify(array, i)


def maxHeapify(array, root):
    mInd = root
    leftChild = (2*root) + 1
    rightChild = (2*root) + 2

    if leftChild <= len(array)-1:
        if array[leftChild] > array[mInd]:
            mInd = leftChild
    if rightChild <= len(array)-1:
        if array[rightChild] > array[mInd]:
            mInd = rightChild
    if mInd != root:
        array[mInd], array[root] = array[root], array[mInd]
    

def heapSort(array):
    tempArr = []
    for i in range(len(array)):
        buildMaxHeap(array)
        array[0], array[len(array)-1] = array[len(array)-1], array[0]
        tempArr.append(array.pop())
    return tempArr