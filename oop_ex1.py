class Laptop :
    def __init__(self, brand_name, model_name, price) :
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + ' ' + model_name

l1 = Laptop('HP', 'Notebook007', 50000)
l2 = Laptop('DELL', 'Preadtor', 60000)

print(l1.brand_name)
print(l1.laptop_name)
print(l2.price)