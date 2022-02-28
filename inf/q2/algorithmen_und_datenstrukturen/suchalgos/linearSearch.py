import random

def linearSearch(l:list, item) -> list:
    for place,i in enumerate(l):
        if i == item:
            return i, place
    return None, None
        
    
def generateList(size:int) -> list:
    l = [x for x in range(size)]
    random.shuffle(l)
    return l


l = generateList(100)
print(l)
print(linearSearch(l,55), l[linearSearch(l,55)[1]])
