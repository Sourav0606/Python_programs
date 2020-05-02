# decorator - enhance the functionallity of other function
# @ use for decorator

def decorator_function(any_function) :
    def wrapper_function() :
        print('This is awsome function')
        any_function()
    return wrapper_function

# This awsome function
@decorator_function  # shortcut call
def func1() :
    print('This is function 1 ')

func1()

@decorator_function
def func2() :
    print('This is function 2 ')

func2()

# func1 = decorator_function(func1)
# func2 = decorator_function(func2)
# func1()
# func2()