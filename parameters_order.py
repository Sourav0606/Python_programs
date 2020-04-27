# PADK

# parameters
# *args
# dafault parameters
# **kwargs

def func(name, *args, last_name = 'unknown', **kwargs) :
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('sourav', 1, 2, 3, a = 1, b = 2)