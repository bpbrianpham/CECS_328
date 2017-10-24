#!python27
import random
import timeit
import math
from search import linearSearch, binarySearch

##Part A
n = int(input("Enter a non-negative integer: "))

array = [None] * n
linearTime = 0
binaryTime = 0
totalTime = 0

for i in range (n):
    l = random.randint(-1001, 1000)
    array[i] = l

array.sort()


for i in range(500):
    k = random.randint(-1, n-1)
    key = array[k]

    start = timeit.default_timer()
    linearSearch(array, key)
    end = timeit.default_timer()
    linearTime += (end - start)

    start = timeit.default_timer()
    binarySearch(array, key)
    end = timeit.default_timer()
    binaryTime += (end - start)

    totalTime += linearTime + binaryTime

print ('******************** PART A **********************')
print ('Linear Search Average Running Time: ' + str((linearTime / 500) * 1000) + ' microsecond(s)')
print ('Binary Search Average Running Time: ' + str((binaryTime / 500) * 1000) + ' microsecond(s)')
print ('Overall Search Average Running Time: ' + str((totalTime / 500) * 1000) + ' microsecond(s)')

##Part B
print ('\n******************** PART B **********************')
print ('n = 100000 or 10^5\n')
n = 100000

array = [None] * n
linearTime = 0
binaryTime = 0
totalTime = 0

for i in range (n):
    l = random.randint(-1001, 1000)
    array[i] = l

array.sort()

key = 5000

start = timeit.default_timer()
linearSearch(array, key)
end = timeit.default_timer()
linearTime += (end - start)

start = timeit.default_timer()
binarySearch(array, key)
end = timeit.default_timer()
binaryTime += (end - start)

totalTime += linearTime + binaryTime

print ('Linear Search Worst-Case Running Time: ' + str(linearTime * 1000) + ' microsecond(s)')
print ('Binary Search Worst-Case Running Time: ' + str(binaryTime * 1000) + ' microsecond(s)')
print ('Overall Search Worst-Case Running Time: ' + str(totalTime * 1000) + ' microsecond(s)')
print ('')
tenPowFiveBinTimePerStep = str((binaryTime / n) * 1000)
print ('Linear Search Worst-Case Running Time Per Step (n = 10^5): ' + str((linearTime / n) * 1000) + ' microsecond(s)')
print ('Binary Search Worst-Case Running Time Per Step (n = 10^5): ' + tenPowFiveBinTimePerStep + ' microsecond(s)')

print ('\n' + 'n = 10000000 or 10^7')
print ('Prediction of linear Search Worst-Case Running Time (n = 10^7): ' 
    + str(((linearTime / n) * 1000) * 10000000) + ' microsecond(s)')
print ('Prediction of binary Search Worst-Case Running Time (n = 10^7): ' 
    + tenPowFiveBinTimePerStep * 10000000) + ' microsecond(s)')
n = 10000000

array = [None] * n
linearTime = 0
binaryTime = 0
totalTime = 0

for i in range (n):
    l = random.randint(-1001, 1000)
    array[i] = l

array.sort()

key = 5000

start = timeit.default_timer()
linearSearch(array, key)
end = timeit.default_timer()
linearTime += (end - start)

start = timeit.default_timer()
binarySearch(array, key)
end = timeit.default_timer()
binaryTime += (end - start)

totalTime += linearTime + binaryTime

print ('Linear Search Worst-Case Running Time (n = 10^7): ' + str(linearTime * 1000) + ' microsecond(s)')
print ('Binary Search Worst-Case Running Time (n = 10^7): ' + str(binaryTime * 1000) + ' microsecond(s)')