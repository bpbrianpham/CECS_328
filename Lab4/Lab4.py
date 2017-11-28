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

print(mssBigOofN(array))