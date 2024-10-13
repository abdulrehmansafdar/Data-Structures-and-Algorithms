import random
numbers =[]
for i in range(25):
    numbers.append(random.randint(-500,500))

print("Numbers: ",numbers)
def RemoveAllNegativeNumbers(array):
    return [num for num in array if num >= 0]
print("Numbers after removing all negative numbers: ",RemoveAllNegativeNumbers(numbers))
def Minimum(array):
    min = array[0]
    
    for num in array:
        if num < min:
            min = num
    return min

def Maximum(array):
    max = array[0]
    
    for num in array:
        if num > max:
            max = num
    return max

def Average(array):
    sum =0
    for i in range(len(array)):
        sum += array[i]
    sum = sum//len(array)
    return sum

# driver code
print("Minimum: ",Minimum(numbers))
print("Maximum: ",Maximum(numbers))
print("Average: ",Average(numbers))



