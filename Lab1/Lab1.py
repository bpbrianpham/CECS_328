import random
import timeit
import math
from search import *

# Prompting user for Array size
n = (int(input("\nEnter an array size: ")))

# Variables for logging search time
bothLinearTime = 0
bothBinaryTime = 0

array = [0] * n

for i in range(n):
    array[i] = random.randint(-1001 , 1000)
    

array.sort()
ToMicrosecond = 1000000
ToMilisecond = 1000
ToSecond = 10000000

# Calculating the timer to find exisitng number
linearTime = 0
binaryTime = 0

for i in range(500):
    temp = random.randint(-1 , n-1)
    key = array[temp]

    start = timeit.default_timer()
    linearSearch(array, key)
    end = timeit.default_timer()
    linearTime = linearTime + (end - start)

    start = timeit.default_timer()
    binarySearch(array, key)
    end = timeit.default_timer()
    binaryTime = binaryTime + (end - start)




# Printing out the loop time
print ("\n********************* Part A *********************")
print ("Average Linear Search Time: " + str((linearTime/500) * ToMicrosecond) + " microseconds")
print ("Average Binary Search Time: " + str((binaryTime/500) * ToMicrosecond) + " microseconds.")


# Calculating the timer to find non-existing number
k = 5000

start = timeit.default_timer()
linearSearch(array, k)
end = timeit.default_timer()
linearTime = end - start

linearTime = (linearTime/n)

start = timeit.default_timer()
binarySearch(array, k)
end = timeit.default_timer()
binaryTime = end - start

binaryTime = (binaryTime/(math.log(n,2)))

print ("\n\n********************* Part B *********************")
# Printing out all Time for searches
print ("One instruction time of Linear Search for n = " + str(n) + ": " + str((linearTime) * ToMicrosecond) + " microseconds.")
print ("One instruction time of Binary Search for n = " + str(n) + ": " + str((binaryTime) * ToMicrosecond) + " microseconds.")

print ("Estimate Time of Linear Search for n = 10^7 : " + str(linearTime * ToSecond) + " seconds")
print ("Estimate Time of Binary Search for n = 10^7 : " + str(binaryTime*(math.log(n,2))) + " seconds ")