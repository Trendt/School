import sys
import random

try:
    n = int(input("n: "))
except Exception:
    print("Only numbers are valid as input!")
    sys.exit(1)

def monte_carlo(n:int):
    k = 0
    for x in range(n):
        x,y = (random.random(), random.random())
        if (x**2 + y**2) <= 1:
            k += 1
    return k/n*4

print(monte_carlo(n))
