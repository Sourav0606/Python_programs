def to_power(pow) :
    def cal_power(value) :
        return value**pow
    return cal_power

cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(4))