def QuickSort(array,start,end):
    if(start<end):
        p_index = partition(array,start,end)
        QuickSort(array,start,p_index-1)
        QuickSort(array,p_index+1,end)
def partition(array,start,end):
    pivot = array[end]
    p_index = start
    for i in range(start,end):
        if array[i]<=pivot:
            array[i],array[p_index ] =array[p_index] ,array[i]
            p_index +=1
    array[p_index],array[end] = array[end],array[p_index]
    return p_index

X = [3,8,15,6,1,7]
QuickSort(X,0,len(X)-1)
print(X)