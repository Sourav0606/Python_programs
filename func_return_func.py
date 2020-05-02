def outer_func(msg) :
    def inner_func() :
        print(f"message is {msg}")
    return inner_func

var = outer_func("hi there !")
var()