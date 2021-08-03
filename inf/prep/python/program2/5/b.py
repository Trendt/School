import sys

try:
    n = int(input("n: "))
    k = int(input("k: "))
except Exception:
    print("Only numbers are allowed as input!")
    sys.exit(1)

def fak(n:int):
    if n == 1:
        return 1;
    return n* fak(n - 1)

def n_over_k(n:int, k:int):
    if n < k:
        return "n has to be greater or equal to k"
    
    return fak(n) / (fak(k) * fak(n - k))

print(n_over_k(n, k))
