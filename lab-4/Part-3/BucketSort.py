
def BucketSort(array):
    n = len(array)
    bucket = []
    for i in range(n):
        bucket.append([])
    for i in range(n):
        index = int(n*array[i])
        bucket[index].append(array[i])
    for i in range(n):
        bucket[i] = InsertionSort(bucket[i])
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k +=1
    return array
def InsertionSort(array):
    n = len(array)
    for i in range(1,n):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j -=1
        array[j+1] = key
    return array

