import funcs
import Prob2
def InsertionSort(array,start,end):
    for i in range(start+1,end+1):
        key = array[i]
        j = i-1
        while j>=start and array[j] > key:
            array[j+1] =array[j]
            j =j -1
        array[j+1]= key
    return array

if __name__== "__main__":
    X = Prob2.RandomArray(500000)
    # X = funcs.Random(0,30000)
    result , runtime = funcs.calculate_time(InsertionSort,X,0,len(X))
    print(result)
    isSorted = funcs.is_sorted(result)
    print(f"Runtime of Insertion sort is : {runtime} where is sorted = {isSorted}")



    import csv
    with open('InsertionSort.csv','w',newline='') as f:

        writer = csv.writer(f)
        for value in result:
            writer.writerow([value])
