import sys

try:
    input_finished = False
    students = []
    while not input_finished:
        student = int(input("Student: "))
        if student != 0:
            students.append(student)
        else:
            input_finished = True
except Exception:
    print("Only numbers are valid as input!")
    sys.exit(0)

def average(l:list):
    return sum(l)/len(l)

print("Min: " + str(min(students)))
print("Max: " + str(max(students)))
print("Average: " + str(average(students)))
