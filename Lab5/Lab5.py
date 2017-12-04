import random
import timeit
import sys
from Heap import *

n = (int(input("\nEnter a positive number: ")))

while (n < 0):
    n = (int(input("\nEnter a positive number: ")))

a = [0] * n

for i in range(n):
    a[i] = (random.randint(-10000, 10000))

#print(a)
heapTimer = 0
sys.setrecursionlimit(1000000)

for i in range(100):
    start = timeit.default_timer()
    a = heapSort(a)
    end = timeit.default_timer()

heapTimer = heapTimer + (end - start)
#print(a)
print (str(heapTimer) + " seconds of heap sorting.")