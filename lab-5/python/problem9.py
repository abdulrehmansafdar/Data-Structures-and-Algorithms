
# list of students
students = []
def AddStudent(name):
    students.append(name)

def PrintStudents():
    for student in students:
        print(student)

def RemoveStudent(name):
    students.remove(name)

if __name__ == "__main__":
    
    print("Add students")
    print("Enter 'q' to quit and r to remove student")
    while True:
        name = input("Enter student name: ")
        if name == 'q':
            break
        elif name == 'r':
            name = input("Enter student name to remove: ")
            RemoveStudent(name)
            continue
        AddStudent(name)
    print("Students added")
    PrintStudents()
