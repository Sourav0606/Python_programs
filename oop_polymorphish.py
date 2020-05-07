# special magic methods / dunder methods
# operator overloading
# polymorphism

class Phone :
    def __init__(self, brand, model_name, price) :
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def full_name(self) :
        return f"{self.brand} {self.model_name}"

    # str, repr

    def __str__(self) :
        return f"{self.brand} {self.model_name} and price is {self._price}"

    def __repr__(self) :
        return f"Phone('{self.brand}', '{self.model_name}', '{self._price}')"

    def __len__(self) :
        return len(self.full_name())

    def __add__(self, other) :
        return self._price + other._price

phone = Phone('Nokia', '1100', 1000)
phone2 = Phone('Nokia', '1100', 1000)
print(str(phone))
print(repr(phone))
print(phone)
print(len(phone))
print(phone + phone2)