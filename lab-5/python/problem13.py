
numbers = [[1,2,3],[4,5,6],[7,8,9]]
print("Numbers Matrix: ")
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j],end=" ")
    print()
def AddColumns(array):
    for i in range(len(array)):
        sum = 0
        for j in range(len(array[i])):
            sum += array[i][j]
        array[i].append(sum)
    return array

def AddRows(array):
    if not array:
        return array  # Return if the array is empty
    row_sums = [0] * len(array[0])
    for row in array:
        for j in range(len(row)):
            row_sums[j] += row[j]
    array.append(row_sums)
    return array

def totalSum(array):
    sum = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            sum += array[i][j]
    return sum

# driver code
print("Numbers Matrix after adding columns: ")
numbers = AddColumns(numbers)
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j],end=" ")
    print()
print("Numbers Matrix after adding rows: ")
numbers = AddRows(numbers)
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j],end=" ")
    print()

print("Total sum of all elements in matrix: ",totalSum(numbers))
