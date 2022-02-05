def fak(number:int) -> int:
    if number > 1:
        return number*fak(number-1)
    elif number == 1:
        return 1
    else:
        print("number needs to be > 0")
        return 0

print(fak(5))

