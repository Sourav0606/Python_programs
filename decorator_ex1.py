from functools import wraps
import time

def calculate_time(function) :
    @wraps(function)
    def wrapper(*args, **kwrgs) :
        print(f"Executing ... {function.__name__}")
        t1 = time.time()
        returned_value = function(*args, **kwrgs)
        t2 = time.time()
        total_time = t2 - t1
        print(f"This function {total_time} second to execute")
        return returned_value
    return wrapper

@calculate_time
def square(n) :
    return [i**2 for i in range(1, n+1)]

print(square(10000))