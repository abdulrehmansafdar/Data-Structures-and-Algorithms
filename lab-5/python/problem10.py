
import time
list =[]
start_time = time.perf_counter()
for i in range(1, 100000 ):
    list.append(i)

end_time = time.perf_counter()
print("Time taken to append 100 elements to list: ", end_time - start_time)
# Answer:
# Yes it takes more time to append if the list is large.