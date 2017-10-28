import random
import timeit
import sys
from Sorting import *


n = int(input("\nPlease enter a positive number: "))

array = [0] * n



repitition = 100

for j in range(repitition):
    for i in range(0, n):
        array[i] = random.randint(-7000 , 7001)
        
    sys.setrecursionlimit(10000)
    
    start = timeit.default_timer()
    array1 = insertionSort(array)
    end = timeit.default_timer()
    insertTimer = end - start


    start = timeit.default_timer()
    array2 = quickSort(array)
    end = timeit.default_timer()
    quickTimer = end - start

#print ("\nInsertion Sort: %s \n" %array)
print ("Insertion Sort takes " + str(insertTimer / repitition) + " seconds\n")

#print ("Quick Sort: %s \n" %array)
print ("Quick Sort takes " + str(quickTimer / repitition) + " seconds\n")

