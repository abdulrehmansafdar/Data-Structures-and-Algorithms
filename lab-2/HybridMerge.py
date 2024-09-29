import funcs
import Prob2
import Insertion
import MergeSort
import time
import csv

def HybridMergeSort(array,start,end,n):
    l = end - start +1
    if(l<=n):
        Insertion.InsertionSort(array,start,end)
    else:
        mid = (start+end)//2
        HybridMergeSort(array,start,mid,n)
        HybridMergeSort(array,mid+1,end,n)
        MergeSort.Merge(array,start,mid,end)

X = Prob2.RandomArray(30000)
if __name__ == "__main__":
    n = 10
    start_time = time.perf_counter()
    HybridMergeSort(X, 2, len(X) - 4, n)
    end_time = time.perf_counter()
    runtime = end_time - start_time

    # print(X)
    isSorted = funcs.is_sorted(X)
    print(f"Runtime of HybridMergeSort is : {runtime} where is sorted = {isSorted}")

    with open('HybridMergeSort.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for value in X:
            writer.writerow([value])


