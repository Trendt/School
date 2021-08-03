size = 20 
table = [[x*y for y in range(1, size+1)] for x in range(1, size+1)] 

def print_table(matrix:list):
    m = max([len(str(x[-1])) for x in matrix])

    for enum, line in enumerate(matrix):
        for part in line:
            print(" "*(m-len(str(part))) + str(part), end=" ")
        print("\n")
    
print_table(table)
