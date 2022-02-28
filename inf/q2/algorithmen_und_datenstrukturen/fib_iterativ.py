from sys import argv

num = int(argv[1])

def fib(n:int) -> int:
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
    return a
    
print(fib(num))
