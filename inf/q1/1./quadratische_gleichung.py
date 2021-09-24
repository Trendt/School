from math import sqrt
from sys import exit

try:
    a = float(input("Koeffizient a:"))
    b = float(input("Koeffizient b:"))
    c = float(input("Koeffizient c:"))
except:
    print("Inputs need to be numbers")

def quadratic_equation(a:float, b:float, c:float) -> list:
    d = b**2 - 4*a*c

    if a == 0:
        if b != 0 :
            return [linear_equation(b, c)]
        elif c != 0:
            return ["n.l."]
        else:
            return ["infinte solutions"]
    else:
        if d > 0:
            return [(-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)]
        elif d == 0:
            return [-b/(2*a)]
        else:
            return ["n.l."]

def linear_equation(m:float, n:float) -> float:
    return -n/m

solutions = quadratic_equation(a,b,c)
print("===================")
print("Solutions:\n" + "\n".join(list(map(str,solutions))))