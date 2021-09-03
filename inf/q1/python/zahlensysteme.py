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

def dec_to_oct(dec:int):
    finished = False
    binary = ""
    while not finished:
        binary += str(dec%8)
        dec = dec//8
        if dec == 0:
            finished = True
    return binary[::-1]

def dec_to_hex(dec:int):
    hex_dict = {
                10:"A",
                11:"B",
                12:"C",
                13:"D",
                14:"E",
                15:"F",
                }

    finished = False
    binary = ""
    while not finished:
        dm = dec%16
        if dm < 10:
            binary += str(dm)
        else:
            binary += hex_dict[dm]
        dec = dec//16
        if dec == 0:
            finished = True
    return binary[::-1]

print("bin:", dec_to_bin(dec))
print("oct:", dec_to_oct(dec))
print("hex:", dec_to_hex(dec))