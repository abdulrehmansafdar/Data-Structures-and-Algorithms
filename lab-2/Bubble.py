
import funcs
import Prob2
def BubbleSort(array,start,end):
    for i in range(start,end):
        for j in range(start,end-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
X = Prob2.RandomArray(30000)
if __name__== "__main__":
    result , runtime = funcs.calculate_time(BubbleSort,X,0,len(X))
    print(result)
    isSorted = funcs.is_sorted(result)
    print(f"Runtime of Bubble sort is : {runtime} where is sorted = {isSorted} ")

    import csv
    with open('BubbleSort.csv','w',newline='') as f:
        writer = csv.writer(f,delimiter='\n')
        writer.writerows([result])