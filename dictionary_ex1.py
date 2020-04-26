def cube_finder(num1) :
    cube_dict = {}
    for i in range(1, num1+1) :
        cube_dict[i] = i**3
    return cube_dict

print(cube_finder(10))