from sys import argv

limit = int(argv[1])

def fib(num:int) -> int:
    if num > 1:
        return fib(num-1) + fib(num-2)
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        print("num has to be > 0")

test_values = [(i, fib(i)) for i in range(0,limit)]
