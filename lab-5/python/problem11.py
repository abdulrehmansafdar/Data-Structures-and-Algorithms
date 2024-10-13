def SerachName(name,array):
    for i in range(len(array)):
        if array[i] == name:
            return i
    return -1

students = ['Ali','Ahmed','Asad','Ahsan','Hamza','John','Jhonny','Jane','Doe','smith','Anderson','Harris','Harrison','Babar','Bilal','Bashir','Bilaw']
name = input("Enter name to search: ")
index = SerachName(name,students)
if index == -1:
    print("Name not found")
else:
    print("Name found at index: ",index)