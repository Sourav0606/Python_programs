fruits = ['grapes', 'apple', 'banana']
print(sorted(fruits))

fruits2 = ('grapes', 'apple', 'banana')
print(sorted(fruits2))

fruits3 = {'grapes', 'apple', 'banana'}
print(sorted(fruits3))

guitars = [
    {'model' : 'yahama f30', 'price' : 8400},
    {'model' : 'faith naptune', 'price' : 50000},
    {'model' : 'faith apollo venus', 'price' : 35000},
    {'model' : 'taylor 814ce', 'price' : 450000}
]

print(sorted(guitars, key = lambda d : d['price']))

sorted_guitars = sorted(guitars, key = lambda d : d['price'], reverse = True)
print(sorted_guitars)