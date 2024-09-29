def CountingSort(array):
    n = len(array)
    
    count_array = [0] * (max(array) + 1)
    for i in range(n):
        count_array[array[i]] +=1
    for j in range(1,len(count_array)):
        count_array[j]+=count_array[j-1]
    output_array =[0]*n
    for i in range(n-1,-1,-1):
        output_array[count_array[array[i]] - 1] = array[i]
        count_array[array[i]] -=1
    return output_array

X = [3,8,15,6,1,7]
result = CountingSort(X)
print(result)


        


    