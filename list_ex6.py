def find_inside_list(l) :
    count = 0
    for i in l :
        if type(i) == list :
            count += 1
    return count

mixed_list = [[1, 2, 3], 5, [1, 2], [6, 7], 9]
print(find_inside_list(mixed_list))