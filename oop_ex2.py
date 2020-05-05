class Laptop :
    def __init__(self, brand_name, model_name, price) :
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + ' ' + model_name

    def apply_discount(self, num) :
        off_price = (num/100)*self.price
        return self.price - off_price


l1 = Laptop('HP', 'Notebook007', 50000)
l2 = Laptop('DELL', 'Preadtor', 60000)

# print(l1.brand_name)
# print(l1.laptop_name)
# print(l2.price)

print(l1.apply_discount(50))