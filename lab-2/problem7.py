import Insertion
import MergeSort
import time
import Selection
import Bubble
import HybridMerge
import Prob2
import csv

# reading values from file one value per line
def read_values():
    with open('Nvalues.txt', 'r') as f:
        lines = f.readlines()
        lines = [int(i) for i in lines if i.strip()]
        return lines

values = read_values()


def calculate_time(func,*args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    runtime = end_time - start_time
    return func.__name__,runtime

filename = "Runtime.csv"
def write_to_csv(name,runtime,n):
    with open (filename,'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name,runtime,n])

for i in values:
    X = Prob2.RandomArray(i)
    # MergeSort
    result , runtime = calculate_time(MergeSort.MergeSort,X,0,len(X)-1)
    formatted_runtime = f"{runtime:.3f}"  # Format runtime to 3 decimal places
    write_to_csv(result, formatted_runtime, i)
for i in values:
    X = Prob2.RandomArray(i)
    # HybridMergeSort
    result , runtime = calculate_time(HybridMerge.HybridMergeSort,X,2,len(X)-4,10)
    formatted_runtime = f"{runtime:.3f}"  # Format runtime to 3 decimal places
    write_to_csv(result, formatted_runtime, i)
for i in values:
    X = Prob2.RandomArray(i)
    # BubbleSort
    result , runtime = calculate_time(Bubble.BubbleSort,X,0,len(X))
    formatted_runtime = f"{runtime:.3f}"  # Format runtime to 3 decimal places
    write_to_csv(result, formatted_runtime, i)
    
for i in values:
    X = Prob2.RandomArray(i)
    # InsertionSort
    result , runtime = calculate_time(Insertion.InsertionSort,X,0,len(X))
    formatted_runtime = f"{runtime:.3f}"  # Format runtime to 3 decimal places
    write_to_csv(result, formatted_runtime, i)
    
for i in values:
    X = Prob2.RandomArray(i)
    # SelectionSort
    result , runtime = calculate_time(Selection.SelectionSort,X,0,len(X))
    formatted_runtime = f"{runtime:.3f}"  # Format runtime to 3 decimal places
    write_to_csv(result, formatted_runtime, i)
    


    
    
