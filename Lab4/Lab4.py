import random
import sys
from mss import *

n = (int(input("\nEnter a positive number: ")))

while (n < 0):
    n = (int(input("\nEnter a positive number: ")))

array = [0] * n

for i in range(n):
    array[i] = random.randint(-100, 100)

print(array)
print("Using MSS O(n) algorithm we get: ")
print(mssBigOofN(array))
print()
sys.setrecursionlimit(100000)
print("Using MSS O(nlogn) algorithm we get: ")
print(mssBigOofNLogN(array, 0, len(array)))