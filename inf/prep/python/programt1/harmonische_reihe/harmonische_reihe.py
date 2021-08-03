from sys import exit

try:
    n = int(input("n: "))
except Exception:
    print("Only numbers allowed as input.")
    exit(1)
    
print("Sum = " + str(sum([1/x for x in range(1, n + 1)])))
