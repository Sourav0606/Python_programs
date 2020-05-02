from functools import wraps
def decorator_function(any_function) :
    @wraps(any_function)
    def wrapper_function(*args, **kwargs) :
        """ this is wrapper function """
        print('This is awsome function')
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func(a) :
    ''' this is func() function '''
    print(f'this is a function with argument {a}')


print(func.__doc__)
print(func.__name__)