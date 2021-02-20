"""
Python's Instance, Class and Static Methods
"""


import math


class Myclass:

    def __init__(self):
        pass

    def method(self):  # it can freely access attributes and other methods
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):  # it cannot modify object instance state
        return 'class method called', cls
    
    @staticmethod
    def staticmethod():  # it can neither modeify object state nor class state
        return 'static method called'


obj = Myclass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())

# the following part is the key:
print(Myclass.staticmethod())
print(Myclass.classmethod())
# print(Myclass.method())  # you are supposed to see an error here


# another example
class Pizza:
    
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'  # !s chooses to use str to format
        # !r choses repr to format the value
        # 'foo {}'.format('bar')
        # 'foo bar'
        # 'foo {!r}'.format('bar')
        # "foo 'bar'"

    def add_newgradient(self, ngd):
        self.ingredients += str(ngd)

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


pz = Pizza('hello')
print(pz)
print(pz.margherita())
print(pz)
pz.add_newgradient('coffee')
print(pz)
print(pz.prosciutto())

# cls implies that method belongs to the class while self implies that the 
# method is related to instance of the class,therefore member with cls is 
# accessed by class name where as the one with self is accessed by instance 
# of the class


# another example
class Pizza:
    
    def __init__(self, ingredients, radius):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'  # !s chooses to use str to format
        # !r choses repr to format the value
        # 'foo {}'.format('bar')
        # 'foo bar'
        # 'foo {!r}'.format('bar')
        # "foo 'bar'"

    def add_newgradient(self, ngd):
        self.ingredients += str(ngd)

    def area(self):
        return self.circle_area(self.radius)  # self could access the static method too

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = Pizza(['mozzarella', 'tomatoes'], 4)
print(p)
print(p.area())
print(Pizza.circle_area(4))