import time 
import random
def calculate_time(func, *args):
    start_time = time.perf_counter()
    ans = func(*args)
    end_time = time.perf_counter()
    runtime = end_time - start_time
    return ans, runtime

def Random(start,end):
    return random.randint(start,end)

def is_sorted(array):
    return all(array[i] <= array[i+1] for i in range(len(array)-1))

# print(is_sorted([1,2,3,4,5,6],1,3))
# print(is_sorted([55,4,2,3,5,7,5,4,7],1,5))