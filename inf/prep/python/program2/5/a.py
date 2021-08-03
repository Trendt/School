import sys

try:
    n = int(input("n: "))
except Exception:
    print("Only numbers are allowed as input!")
    sys.exit(1)

def fak(n:int):
    if n == 1:
        return 1;
    return n* fak(n - 1)

print(fak(n))
