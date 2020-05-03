def even_value(n) :
    for i in range(1, n+1) :
        if i % 2 == 0 :
            yield(i)

eve = even_value(20)
for i in eve :
    print(i)