import sys


try:
    n = int(input("n: "))
except:
    print("Only numbers are valid as input!")
    sys.exit(1)

def rect(n:int):
    print(n*"*")
    for x in range(n):
        print("*" + " "*(n-2) + "*")
    print(n*"*")

def triangle_left(n:int):
    for x in range(1, n+1):
        print("*"*x)

def triangle_right(n:int):
    for x in range(1, n+1):
        print(" "*(n-x) + "*"*x)

def hourglass(n:int):
    if n % 2 != 1:
        n -= 1
    for x in range(n, 1, -2):
        print(" "*int((n-x)/2) + "*"*x)

    print(" "*int((n-1)/2) + "*")

    for x in range(3, n+1, 2):
        print(" "*int((n-x)/2) + "*"*x)

rect(n)
print("\n")

triangle_left(n)
print("\n")

triangle_right(n)
print("\n")
hourglass(n)
