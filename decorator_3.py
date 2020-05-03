from functools import wraps

def print_function_data(any_function) :
    @wraps(any_function)
    def wrapping_function(*args, **kwargs) :
        print(f"you are calling {any_function.__name__} function")
        print(f"{any_function.__doc__}")
        return any_function(*args, **kwargs)
    return wrapping_function

@print_function_data
def add(a, b) :
    '''This function takes 2 number as arguments and return there sum '''
    return a+b

print(add(3, 5))