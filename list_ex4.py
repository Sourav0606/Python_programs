def odd_even(l) :
    odd_list = []
    even_list = []
    elements_list = []
    for i in l :
        if i % 2 == 0 :
            even_list.append(i)
        else :
            odd_list.append(i) 
    elements_list = [odd_list, even_list]
    return elements_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(odd_even(numbers))   