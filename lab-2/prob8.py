import time
import csv
import MergeSort  
import Selection
def read_values():
    with open('words.txt', 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines if line.strip()]

def calculate_time(func, *args):
    start_time = time.perf_counter()
    func(*args)  
    end_time = time.perf_counter()
    runtime = end_time - start_time
    return runtime,func.__name__

filename = "WordsRuntime.csv"
def write_to_csv(name, runtime, words):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, runtime] + words)

def Shuffle(words):
    import random
    random.shuffle(words)

if __name__ == "__main__":
    words = read_values()  
    runtime,name = calculate_time(MergeSort.MergeSort, words, 0, len(words) - 1)
    formatted_runtime = f"{runtime:.6f}" 
    # Write the sorted list to the CSV file
    write_to_csv(name, formatted_runtime, words)
    runtime_selection,name_1=calculate_time(Selection.SelectionSort,words,0,len(words)-1)
    formatted_runtime_1 = f"{runtime_selection:.6f}" 
    write_to_csv(name_1,formatted_runtime_1,words)

    # shuffle the list and sort it again
    Shuffle(words)
    runtime,name = calculate_time(MergeSort.MergeSort, words, 0, len(words) - 1)
    formatted_runtime = f"{runtime:.6f}"
    write_to_csv(name, formatted_runtime, words)
    runtime_selection,name_1=calculate_time(Selection.SelectionSort,words,0,len(words)-1)
    formatted_runtime_1 = f"{runtime_selection:.6f}"
    write_to_csv(name_1,formatted_runtime_1,words)


