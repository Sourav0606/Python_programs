def common_elements(l1, l2) :
    temp = []
    for i in l1 :
        if i in l2 :
            temp.append(i)
    return temp

lst1 = [1, 2, 5, 8]
lst2 = [1, 2, 7, 6]
print(common_elements(lst1, lst2))
