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


test_data = [7,34,5,52,34,234,267,3,54,46,24,23,421,4,7,89,3452,3]
sorted = insertionSort(test_data)
print(test_data)
print(sorted)
