# map
def square(a) :
    return a**2

l = [1, 2, 3, 4, 5]
# print(list(map(square, l)))
print(list(map(lambda a : a**2, l)))

def my_map(func, l) :
    my_list = []
    for item in l :
        my_list.append(func(item))
    return my_list

def my_map2(func, l) :
    return [func(item) for item in l]

print(list(my_map(lambda a : a**3, l)))
print(list(my_map2(lambda a : a**3, l)))