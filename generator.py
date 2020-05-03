def nums(n) :
    for i in range(1, n+1) :
        yield(i)
    
numbers = nums(10)

for num in numbers :
    print(num)

for num in numbers : # generator or itrable can be use only once
    print(num)