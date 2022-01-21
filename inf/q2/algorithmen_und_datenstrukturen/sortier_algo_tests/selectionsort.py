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
        print("del", del_index, "  list:", item_copy) 
        item_copy.pop(del_index)
    return sorted

test_data = [921,23,13,5,1,2,3,6,8,3,34,5,2,34,26,234,2,34,234,7,23,42,7,3,7,7,94,76,73,46]
sorted = selectionSort(test_data)
print(test_data, "n", sorted, "\n\n")
print(len(test_data), len(sorted))
