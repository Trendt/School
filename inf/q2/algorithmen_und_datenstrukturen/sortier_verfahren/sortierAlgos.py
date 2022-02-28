from random import randint

def generateList(size:int=100):
    return [randint(0,size) for _ in range(size)]

def insertionSort(item:list) -> list:
    item_copy = item[1:].copy()
    sorted = [item[0]]
    while item_copy != []:
        current_item = item_copy[0] 
        item_copy.pop(0)

        for index, item in enumerate(sorted):
            if item <= current_item:
                insertion_index = index+1
            else:
                insertion_index = index
                break
        sorted.insert(insertion_index, current_item)
    return sorted
    
def quicksort(l:list) -> list:
    if len(l) == 0:
        return l
    pivot = 0
    kleiner = [i for i in l if i < l[pivot]]
    gleich = [i for i in l if i == l[pivot]]
    groesser = [i for i in l if i > l[pivot]]
    return quicksort(kleiner) + gleich + quicksort(groesser)

def quicksort_oneline(l:list)->list:
    return quicksort([i for i in l if i < l[0]]) + [i for i in l if i == l[0]] + quicksort([i for i in l if i > l[0]]) if len(l) != 0 else l

liste = generateList(100000)
print("ganze liste:", liste)
print(liste)
