class Circle :
    pi = 3.14
    def __init__(self, radius) :
        self.radius = radius

    def calc_circumference(self) :
        return 2*Circle.pi*self.radius

c1 = Circle(2)
c2 = Circle(6)
print(c1.calc_circumference())
print(c2.calc_circumference())

class Laptop :
    discount_percentage = 10
    def __init__(self, brand_name, model_name, price) :
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + ' ' + model_name

    def apply_discount(self) :
        off_price = (self.discount_percentage/100)*self.price
        return self.price - off_price


l1 = Laptop('HP', 'Notebook007', 50000)
l2 = Laptop('DELL', 'Preadtor', 60000)
l2.discount_percentage = 50
print(l2.__dict__)
print(l1.apply_discount())
print(l2.apply_discount())