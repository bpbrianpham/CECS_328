import random
import timeit
import sys
from Sorting import *


n = (int(input("\nPlease enter a positive number: ")))

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

#print ("\nInsertion Sort: %s \n" %array)
print ("Insertion Sort takes " + str(insertTimer / repitition) + " seconds on average\n")

#print ("Quick Sort: %s \n" %array)
print ("Quick Sort takes " + str(quickTimer / repitition) + " seconds on average\n")

