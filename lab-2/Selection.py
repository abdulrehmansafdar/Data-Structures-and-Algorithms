import funcs
import Prob2

def SelectionSort(array,start,end):
    n = end 

    for j in range (start,n):

        min = j

        for i in range(j+1,n):

            if(array[i]<array[min]):
                min  = i

        array[j] , array[min] = array[min] ,array[j]
    return array
X = Prob2.RandomArray(10)



if __name__== "__main__":
    result , runtime = funcs.calculate_time(SelectionSort,X,2,7)
    print(funcs.is_sorted(result[2:7]))
    print(result)


    print(f"Array is sorted in {runtime}")



    