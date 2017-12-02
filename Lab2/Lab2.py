import random
import timeit
import math
import sys
from Sorting import *


n = (int(input("\nPlease enter a positive number: ")))
print()
array = [0] * n

repitition = 100

insertTimer = 0
quickTimer = 0

for j in range(repitition):
    for i in range(len(array)):
        array[i] = random.randint(-7001, 7000)

        
    sys.setrecursionlimit(10000)
    
    start = timeit.default_timer()
    array1 = insertionSort(array)
    end = timeit.default_timer()
    insertTimer = insertTimer + (end - start)
    

    start = timeit.default_timer()
    array2 = quickSort(array)
    end = timeit.default_timer()
    quickTimer = quickTimer + (end - start)

averageInsertRunTime = insertTimer / repitition
averageQuickRunTime = quickTimer / repitition
print ("Insertion Sort takes " + str(averageInsertRunTime) + " seconds on average\n")

print ("Quick Sort takes " + str(averageQuickRunTime) + " seconds on average\n")

print ("This computer runs: " + str(math.pow(n, 2) / averageInsertRunTime) + " instructions per seconds\n")

