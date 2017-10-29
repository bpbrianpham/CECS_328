import random
import sys
from QuickSearch import quickSearch

n = (int(input("\nEnter a positive number: ")))

array = [0] * n

for i in range(n):
    array[i] = random.randint(-100, 100)

print(array)

k = (int(input("\n\nEnter a number between 1 and the number you picked: ")))
while(k > n):
    k = (int(input("\nEnter a number between 1 and the number you picked: ")))

sys.setrecursionlimit(10000000)
print("The " + str(k) + "th least number is: " + str(quickSearch(array, k)) + "\n\n")