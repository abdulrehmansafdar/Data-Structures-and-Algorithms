import funcs
def RandomArray(size):
    random_array =[]
    for i in range(size):
        n = funcs.Random(-150000,150000)
        random_array.append(n)
    return random_array

if __name__== "__main__":
    result , runtime = funcs.calculate_time(RandomArray,2000)
    print(f"Array {result} is populated in {runtime}")
