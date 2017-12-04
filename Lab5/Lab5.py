import random
import timeit
import sys
from Heap import *
from SelectionSort import *
from Sorting import *

n = (int(input("\nEnter a positive number: ")))

while (n < 0):
    n = (int(input("\nEnter a positive number: ")))

a = [0] * n
b = [0] * n
c = [0] * n

for i in range(n):
    randNum  = (random.randint(-10000, 10000))
    a[i] = randNum
    b[i] = randNum
    c[i] = randNum


quickTimer = 0
heapTimer = 0
selectTimer = 0

sys.setrecursionlimit(10000)

startQuick = timeit.default_timer()
quickSort(a)
endQuick = timeit.default_timer()
quickTimer = quickTimer + (endQuick - startQuick)
print (str(quickTimer) + " seconds of quick sorting.")

startSelect = timeit.default_timer()
selectionSort(b)
endSelect = timeit.default_timer()
selectTimer = selectTimer + (endSelect - startSelect)
print (str(selectTimer) + " seconds of selection sorting.")

startHeap = timeit.default_timer()
heapSort(c)
endHeap = timeit.default_timer()
heapTimer = heapTimer + (endHeap - startHeap)
print (str(heapTimer) + " seconds of heap sorting.")