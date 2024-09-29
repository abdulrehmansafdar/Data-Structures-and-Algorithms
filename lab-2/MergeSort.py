import funcs
import Prob2
import time
def MergeSort(array,start,end):
    if(start<end):
        mid = (start+end)//2
        MergeSort(array,start,mid)
        MergeSort(array,mid+1,end)

        Merge(array,start,mid,end)

def Merge(array,start,mid,end):
    L = mid -start+1
    R = end- mid
    L_array = array[start:mid+1]
    R_array = array[mid+1:end+1]
    i=0
    j=0
    
    
    k=start
    while(i<len(L_array) and j<len(R_array)):
        if(L_array[i]<=R_array[j]):
            array[k] = L_array[i]
            i+=1
        else:
            array[k] = R_array[j]
            j+=1
        k+=1

    while(i<L):
        array[k] =L_array[i]
        k+=1
        i+=1
    while(j<R):
        array[k] = R_array[j]
        j+=1
        k+=1
    return array

X = [3,8,15,6,1,7]

if __name__ == "__main__":
    
    MergeSort(X, 0, len(X) - 1)
    

    print(X)
    
    
    

    
