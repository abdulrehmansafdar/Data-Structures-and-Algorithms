def RadixSort(array):
    max1 = max(array)
    exp = 1
    while max1/exp >0:
        CountingSort(array,exp)
        exp *=10
def CountingSort(array,exp):
    n = len(array)
    count_array = [0] * 10
    output_array = [0] * n
    for i in range(n):
        index = array[i]//exp
        count_array[index%10] +=1
    for j in range(1,10):
        count_array[j] += count_array[j-1]
    for i in range(n-1,-1,-1):
        index = array[i]//exp
        output_array[count_array[index%10]-1] = array[i]
        count_array[index%10] -=1
    for i in range(n):
        array[i] = output_array[i]
X = [3,8,15,6,1,7]
RadixSort(X)
print(X)