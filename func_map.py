# map function
numbers = [1, 2, 3, 4, 5]

#  def square(a) :
#      return a**2

#squares = list(map(square, numbers))
squares = list(map(lambda a : a**2, numbers))
print(squares)

# list comp
squares_new = [i**2 for i in range(1, 11)]
print(squares)

names = ['abc', 'abcd', 'abcde']
length = map(len, names)  # length = list(map(len, names))
for i in length :
    print(i)