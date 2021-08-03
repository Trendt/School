import sys

try:
    n = int(input("number: "))
except Exception:
    print("Only numbers are valid as input!")
    sys.exit(1)

def rom_to_dec(n:int):
    numbers = [[1, "I"], [4, "IV"],
                [5, "V"], [9, "IX"],
                [10, "X"], [40, "XL"],
                [50, "L"], [90, "XC"],
                [100, "C"], [400, "CD"],
                [500, "D"], [900, "DM"],
                [1000, "M"]]
    numbers.sort(key = lambda x: x[0], reverse = True)

    print(numbers)
    rom = ""
    for x in numbers:
        if n >= x[0]:
            rom += x[1] * (n//x[0])
            n = n % x[0]
            
    return rom

print(rom_to_dec(n))
