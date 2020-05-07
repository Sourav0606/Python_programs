class A :

    def class_a_method(self) :
        return 'class A method called'

    def hello(self) :
        return 'hello form class A'

class B :

    def class_b_method(self) :
        return 'class B method called'

    def hello(self) :
        return 'hello form class B'

class C(A, B) :
    pass

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello()) # using mro
print(help(C))
print(C.mro())
print(C.__mro__)