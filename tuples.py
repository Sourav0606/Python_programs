mixed = (1, 2, 3, 4.0)

##for loop with tuple
# for i in mixed :
#     print(i)

## tuple with one element
# nums = (1,)  # should be , after any element
# words = ('word1',)
# print(type(nums))
# print(type(words))

## tuple without paranthesis
guitars = 'abc', 'def', 'xyz'
# print(type(guitars))

## tuple unpacking
guitarist = ('xyz', 'abx', 'def')
guitarist1, guitarist2, guitarist3 = (guitarist)
# print(guitarist3)

## list inside tuple
favorites = ('tuples', ['element of list', 'abc'])
favorites[1].pop()
favorites[1].append("done")
# print(favorites)

## functions
## min(), max(), sum()