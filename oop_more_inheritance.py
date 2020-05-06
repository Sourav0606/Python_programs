# can we derive more then one class form base class ?
# multilevel inheritance
# method resolutoin order
# method overriding
# isinstance(), issubclass()

class Phone :
    def __init__(self, brand, model_name, price) :
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def make_a_call(self, phone_number) :
            print(f"calling {phone_number}")

    def full_name(self) :
        return f"{self.brand} {self.model_name}"

class Smartphone(Phone) :
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera) :
        # Phone.__init__(self, brand, model_name, price)
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    
    def full_name(self) :
        return f"{self.brand} {self.model_name} and price is {self._price}"

class FlagshipPhone(Smartphone) :
        def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, fornt_camera) :
            super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
            self.fornt_camera = fornt_camera
        
        def full_name(self) :
            return f"{self.brand} {self.model_name} and price is {self._price} and rear camera is {self.rear_camera}"

phone = Phone('Nokia', '1100', 1000)
smartphone = Smartphone('onePlus', '8', 40000, '6 GB', '128 GB', '64 MP')
flagshipPhone = FlagshipPhone('onePlus', '8 pro', 50000, '6 GB', '128 GB', '64 MP', '24 MP')
print(phone.full_name())
print(smartphone.full_name())
print(flagshipPhone.full_name())
# print(help(Smartphone)) # to find method resolution order
print(isinstance(smartphone, Phone))
print(isinstance(flagshipPhone, Phone))
print(issubclass(Smartphone, Phone))
print(issubclass(FlagshipPhone, Phone))
