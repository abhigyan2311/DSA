'''
Builder is a creational design pattern that lets you construct complex objects
step by step. The pattern allows you to produce different types and 
representations of an object using the same construction code.
'''


'''
Builder patter not needed in Python because it supports named parameters
'''

class SomeClass(object):
    def __init__(self, foo="default foo", bar="default bar", baz="default baz"):
        pass

s = SomeClass(bar=1, foo=0)

'''
Note that you can freely reorder and omit arguments, 
just as with a builder in Java you can omit or reorder calls to the set methods on the builder object.
'''

class Pizza:
    def __init__(self) -> None:
        self.ketchup = False
        self.cheese = False
        self.tomato = False
        self.onion = False
    
    def set_ketchup(self):
        self.ketchup = True
    
    def set_cheese(self):
        self.cheese = True
    
    def set_tomato(self):
        self.tomato = True
    
    def set_onion(self):
        self.onion = True

pizza1 = Pizza()
pizza1.set_cheese()
pizza1.set_tomato()
pizza1.set_onion()

pizza2 = Pizza()
pizza2.set_cheese()
pizza2.set_ketchup()
    