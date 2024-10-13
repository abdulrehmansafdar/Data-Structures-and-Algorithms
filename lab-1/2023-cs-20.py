


# Problem 1.1
def find(array, value):
    indices = []
    for i in range(len(array)):
        if array[i] == value:
            indices.append(i)
    return -1 if len(indices) == 0 else indices




#Problem 1.2  
X = [1,2,2,5,7,9,11,13,22]
a = 2
result = find(X,a)
if (result == -1):
    print("The number is not in the list")
else:
    print("The number is in the list at index: ",result)



# Problem 1.3

def Minimum(array,starting_index,ending_index):
    min = array[starting_index]
    for i in range(starting_index,ending_index+1):
        if(array[i]<min):
            return i
    return starting_index
    


# problem 1.4
def sort(array):
    
    for i in range(len(array)):
        min_index = Minimum(array,i,len(array)-1)
        array[i], array[min_index] = array[min_index], array[i]
    return array


   

# problem 1.5
def get_given_part_of_string(string,starting_index,ending_index):
    sub_string = string[starting_index:ending_index+1]
    rev_string = sub_string[::-1]
    return rev_string

#problem 1.6

def iterative_sum(num):
    num_str= str(num)
    sum = 0
    for i in range(len(num_str)):
        sum += int(num_str[i])
    return sum
def recursive_sum(num):
    num_str = str(num)
    if(len(num_str)==1):
        return int(num_str)
    else:
        return int(num_str[0]) + recursive_sum(int(num_str[1:]))

# Problem 1.7

def Column_wise_sum(matrix):
    column_sum =[]
    for i in range (len(matrix[0])):
        sum =0
        for j in range(len(matrix)):
            sum += matrix[j][i]
        column_sum.append(sum)
    return column_sum
def Row_wise_sum(matrix):
    row_sum =[]
    for i in range (len(matrix)):
        sum =0
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
        row_sum.append(sum)
    return row_sum


#problem 1.8
def sort_two_sorted_array(arr1,arr2):
    merged_array =[]
    i = 0
    j = 0
    while(i<len(arr1) and j < len(arr2)):
        if(arr1[i]< arr2[j]):
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while(i<len(arr1)):
        merged_array.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        merged_array.append(arr2[j])
        j+=1
    return merged_array
    
#Problem 1.9
def is_palindrome(string):
    if(len(string)<=1):
        return True
    if(string[0] != string[-1]):
        return False
    return is_palindrome(string[1:-1])

#problem 1.10
def Sort_neg_pos(arr):
    neg =[]
    pos =[]
    for i in range (len(arr)):
        if(arr[i]<0):
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    sorted_neg = sort(neg)
    sorted_pos = sort(pos)
    merged_array =[]
    i = 0
    j=0
    k=0
    while(i<len(sorted_neg) and i<len(sorted_pos)):
        if k%2 ==0:
            merged_array[k] = neg[i]
            i+=1
            k+=1
        elif k%2 ==1:
            merged_array[k] = pos[j]
            j+=1
            k+=1
    return merged_array
X =[10, -1, 9, 20, -3, -8, 22, 9, 7]
print(Sort_neg_pos(X))
    
  
        
