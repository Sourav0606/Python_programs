def is_even(a) :
    return a % 2 == 0

numbers = [2, 7, 1, 8, 0, 9, 4, 5]

# evens = list(filter(is_even, numbers))
evens = list(filter(lambda a : a % 2 == 0, numbers))
print(evens)

# evens = filter(is_even, numbers)
# for i in evens :
#     print(i)

# list comp
new_evens = [i for i in numbers if i % 2 == 0]
print(new_evens)