import sys

try:
    n = int(input("n = "))
except Exception:
    print("Input needs to be a number of type integer!")
    exit(1)


numbers = [x for x in range(1, n+1, 2)]
print("Summe: " + str(sum(numbers)))
print("Anzahl gerader Zahlen: " + str(len(numbers)))
