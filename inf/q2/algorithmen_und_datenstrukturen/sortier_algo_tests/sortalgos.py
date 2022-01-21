from random import randint
from time import *

def bubbleSort(item:list) -> list:
    list_copy = item.copy()

    for _ in range(len(item)):
        l = list_copy.copy()
        for index, i in enumerate(l[:-1]):
            if i > l[index+1]:
                list_copy[index], list_copy[index+1] = list_copy[index+1], list_copy[index]

    return list_copy

def selectionSort(item:list) -> list:
    sorted = []
    item_copy = item.copy()
    for _ in range(len(item)):
        minimum = item_copy[0]
        for index, num in enumerate(item_copy):
            if num <= minimum:
                minimum = num
                del_index = index
        sorted.append(minimum)
        item_copy.pop(del_index)
    return sorted

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

test_data = [randint(0,10000) for i in range(10000)]

t1 = time()
print(t1)
selectionSort(test_data)
t2 = time()
print(t2)
runtime = t2-t1
print("runtime:", runtime)
