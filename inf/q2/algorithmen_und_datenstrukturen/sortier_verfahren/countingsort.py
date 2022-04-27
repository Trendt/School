from random import randint
// erstelle eine liste mit 1000 zufällig gewählten zahlen von 0-100000
unsorted_list = [randint(0,100000) for x in range(1000)]
print(unsorted_list)

def countingSort(l:list) -> list:
    // erstelle counting liste mit einer länge von max + 1
    cl = [0] * (max(l) + 1)
    // ergebnisliste
    rl = []

    for i in l:
        cl[i]+=1
    for enum,j in enumerate(cl):
        rl += [enum] * j
    return rl

print(countingSort(unsorted_list))
