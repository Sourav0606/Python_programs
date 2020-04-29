# without using enumerate function
# names = ['abc', 'asdff', 'sourav']
# pos = 0
# for name in names :
#     print(f"{pos} -----> {name}")
#     pos += 1

# with enumerator function
names = ['abc', 'asdff', 'sourav']
# for pos, name in enumerate(names) :
#     print(f"{pos} -----> {name}")

def find_pos(l, s) :
    for pos, name in enumerate(l) :
        if name == s :
            return pos
    return -1

print(find_pos(names, 'sourav'))
