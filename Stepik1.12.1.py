import math
from math import sqrt
a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
#print(pow((p * (p-a) * (p-b) * (p-c)), 0.5))
print(sqrt((p * (p-a) * (p-b) * (p-c))))