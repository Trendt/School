def bubbleSort(item:list) -> list:
    list_copy = item.copy()

    for _ in range(len(item)):
        l = list_copy.copy()
        for index, i in enumerate(l[:-1]):
            if i > l[index+1]:
                list_copy[index], list_copy[index+1] = list_copy[index+1], list_copy[index]

    return list_copy

    
test = [1,23,562,3,42,62,5,3,234,2,423,4,78,34,3,46,235,8,324,234,1,414]
sorted = bubbleSort(test)
print(test, sorted)

