def square_list(l) :
    square = []
    for i in l :
        square.append(i**2)
    return square

number = list(range(1, 11))
print(square_list(number))