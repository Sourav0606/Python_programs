# fromkeys

# d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
# print(d)

# get method (useful)
d = {'name' : 'sourav', 'age' : 21}
# print(d.get('age'))

# if d.get('name') :
#     print('present')
# else :
#     print('not present')

# clear method
# d.clear()
# print(d)

# copy method

d1 = d.copy() # it create two different dictionaries
# d1 = d  # both will same

print(d1 is d)