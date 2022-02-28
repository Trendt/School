def fak(number:int) -> int:
    if number > 1:
        return number*fak(number-1)
    elif number == 1:
        return 1
    else:
        print("number needs to be > 0")
        return 0

def faki(number:int) -> int:
    a = 1
    for i in range(1,number+1):
        a *= i
    return a
        
print(fak(5))
print(faki(5))
