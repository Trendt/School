import random

def binarySearch(l:list,low, high, i) -> tuple:
    mid = (low + high)//2
    if i == l[mid]:
        return mid
    elif i < l[mid]:
        return binarySearch(l, low, mid, i)
    else:
        return binarySearch(l, mid, high, i)

def binarySearchIter(l:list, obj):
    links=mitte=rechts=0
    rechts = len(l)-1
    while links <= rechts:
        mitte = (rechts+links)//2

        if l[mitte] < obj:
            links = mitte + 1
        elif l[mitte] > obj:
            rechts = mitte - 1
        else:
            return mitte

    return None
            
    
l = [x for x in range(1000)]
result = binarySearchIter(l, 555)
print(result, l[result])
