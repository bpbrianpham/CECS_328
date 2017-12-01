import random
import timeit
import sys
from Heap import *

n = (int(input("\nEnter a positive number: ")))

while (n < 0):
    n = (int(input("\nEnter a positive number: ")))

arr = [0] * n

for i in range(n):
    arr[i] = (random.randint(-10000, 10000))

print(arr)
heapTimer = 0
sys.setrecursionlimit(1000000)

#for i in range(100):
start = timeit.default_timer()
print(heapSort(arr))
end = timeit.default_timer()

heapTimer = heapTimer + (end - start)

print (str(heapTimer) + " seconds of heap sorting.")