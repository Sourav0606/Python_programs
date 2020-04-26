# in keyword and iterations in dictionary

user_info = {
    'name' : 'sourav',
    'age' : 21,
    'fav_movies' : ['movie1', 'movie2'],
    'fav_tunes' : ['tunes1', 'tunes2'],
}

# check if key exist in dictionary
# if 'name' in user_info :
#     print('present')
# else :
#     print('not present')

# # check if value exist in dictionary
# if 'sourav' in user_info.values() :
#     print('present')
# else :
#     print('not present')

#loops in dictionaries
# for i in user_info() :
#     print(i)

# values method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# loops in dictionaries
# for i in user_info :
#     print(user_info[i])

# item method
# user_item = user_item.items()
# print(user_item)
# print(type(user_item))

for key, value in user_info.items() :
    print(f'key is {key} and value is {value}')