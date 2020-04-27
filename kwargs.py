def func(**kwargs) :
    for k, v in kwargs.items() :
        print(f"{k} : {v}")
    
d = {
    'name' : 'sourav',
    'age' : 21
}
func(**d)
# func(first_name = 'sourav', last_name = 'rai')