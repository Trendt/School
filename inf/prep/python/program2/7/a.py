import sys

try:
    n = int(input("Schülerzahl: "))
    students = [int(input("Schüler: ")) for x in range(n)]
except Exception:
    print("Only numbers are valid as input!")
    sys.exit(0)

def average(l:list):
    return sum(l)/len(l)

print("Min: " + str(min(students)))
print("Max: " + str(max(students)))
print("Average: " + str(average(students)))
