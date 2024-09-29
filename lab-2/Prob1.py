
import funcs

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
result, runtime = funcs.calculate_time(factorial,900)
print(f"Runtime of factorial function is : {runtime}")