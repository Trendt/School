import sys


try:
    n = int(input("Obergrenze: "))
except Exception:
    print("Only numbers are valid as input!")
    sys.exit(1)

possibilities = [(a, b, c) for a in range(1, n+1) for b in range(1,n+1) for c in range(1, n+1) ]
#print(possibilities)
tripel = []
for p in possibilities:
    if p[0]**2 + p[1]**2 == p[2]**2:
        tripel.append(f"{p[0]}^2 + {p[1]}^2 == {p[2]}^2")

for t in tripel:
    print(t)
