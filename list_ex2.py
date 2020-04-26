def reverse_list(l) :
    reversed_list = []
    for i in range(len(l)) :
        popped_item = l.pop()
        reversed_list.append(popped_item) 
    return reversed_list

items = list(range(1, 11))
print(reverse_list(items))