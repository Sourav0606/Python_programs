user_info = {
    'name' : 'sourav',
    'age' : 21,
    'fav_movies' : ['movie1', 'movie2'],
    'fav_tunes' : ['tunes1', 'tunes2'],
}

more_info = {
    'name' : 'sourav rai',
    'state' : 'rajasthan',
    'hobbies' : ['coding', ['gaming']]
}

user_info.update(more_info)
print(user_info)