class Person :
    count_instance = 0
    def __init__(self, first_name, last_name, age) :
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls, string) :    
        first, last, age = string.split(',')
        return cls(first, last, int(age))

    @classmethod
    def count_instances(cls) :
        return f"You have created {cls.count_instance} instance of {cls.__name__} class"
        # return f"You have created {cls.count_instance} instance of Person class"
 
    @staticmethod
    def hello() :
        print("Hello, static method called")

    def full_name(self) :
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self) :
        return self.age > 18 

p1 = Person('Sourav', 'Rai', 21)
p2 = Person('Guddu', 'Rai', 19)
p3 = Person.from_string('xyz, aa, 20')

print(p3.full_name())
print(p3.is_above_18())
Person.hello()