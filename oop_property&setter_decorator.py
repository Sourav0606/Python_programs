class Phone :
    def __init__(self, brand, model_name, price) :
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)
        # if price > 0 :
        #     self._price = price
        # self._price = 0
        # self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}"

    def complete_specification(self) :
        return f"{self.brand} {self.model_name} and price is {self._price}"

    # getter(), setter()

    @property
    def price(self) :
        return self._price

    @price.setter
    def price(self, new_price) :
        self._price = max(new_price, 0)

    def make_a_call(self, phone_number) :
        print(f"calling {phone_number}")

    def full_name(self) :
        return f"{self.brand} {self.model_name}"

phone1 = Phone('Nokia', '1100', 1000)
# print(phone1.brand)
# print(phone1.model_name)
phone1.price = -500
print(phone1._price)
print(phone1.complete_specification())
# for @property using in the function for
# print(phone1.complete_specification)