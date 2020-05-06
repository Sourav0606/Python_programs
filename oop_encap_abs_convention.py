# Encapsulation
# Abstraction
# Some special naming convention
# Name Mangling

class Phone :
    def __init__(self, brand, model_name, price) :
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def make_a_call(self, phone_number) :
        print(f"calling {phone_number} ")
    
    def full_name(self) :
        return f"{self.brand} {self.model_name}"

phone1 = Phone('iPhone', 'x', 100000)
print(phone1.price)
print(_phone1._phone)