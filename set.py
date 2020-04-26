s = {1,2,3,2}
# l = [1,2,3,4,55,5,5,6,7,8,8,8,8,9]
# remove duplicate
# s2 = list(set(l))
# print(s2)
s.add(4)
s.add(5)
s.remove(3) #if 3 is not present then it will show error so use discard
s.discard(5) # it will not show any error
print(s)
