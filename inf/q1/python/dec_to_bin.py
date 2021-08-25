from sys import exit, stderr

try:
    i = input("Dezimalzahl: ")
    dec = int(i)
except:
    # print(f"input is type {type(i)}, needs to be integer", file=stderr)
    print("Not a valid input")
    exit(1)

def dec_to_bin(dec:int):
    finished = False
    binary = ""
    while not finished:
        binary += str(dec%2)
        dec = dec//2
        if dec == 0:
            finished = True
    return binary[::-1]

print(dec_to_bin(dec))
