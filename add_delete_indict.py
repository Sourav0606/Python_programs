# add and delete in dictionary

user_info = {
    'name' : 'sourav',
    'age' : 21,
    'fav_movies' : ['movie1', 'movie2'],
    'fav_tunes' : ['tunes1', 'tunes2'],
}

# how to add data
# user_info['fav_songs'] = ['song1', 'song2']
# print(user_info)

# pop method
# popped_item = user_info.pop('fav_movies')
# print(f'popped item is {popped_item}')
# print(user_info)

# popitem method
popped_item = user_info.popitem()
print(user_info)
print(popped_item)