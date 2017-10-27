import random
import timeit
import sys
from Sorting import *


n = int(input("\nPlease enter a positive number: "))

array = [0] * n

for i in range(n):
    l = random.randint(-7000 , 7001)
    array[i] = l

sys.setrecursionlimit(10000)
start = timeit.default_timer()
array1 = insertionSort(array)
end = timeit.default_timer()
insertTimer = end - start
#print ("\nInsertion Sort: %s \n" %array)
print ("Insertion Sort takes " + str(insertTimer * 1000) + " microseconds\n\n")

start = timeit.default_timer()
array2 = quickSort(array)
end = timeit.default_timer()
quickTimer = end - start
#print ("Quick Sort: %s \n" %array)
print ("Quick Sort takes " + str(quickTimer * 1000) + " microseconds\n\n")

