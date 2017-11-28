import random
import sys
import mss

n = (int(input("\nEnter a positive number: ")))

while (n < 0):
    n = (int(input("\nEnter a positive number: ")))

a = [0] * n

for i in range(n):
    array[i] = random.randint(-100, 100)

print(mssBigOofN(a))