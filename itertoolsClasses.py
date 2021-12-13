#  #  #  #  #  #  #  #  #  #  #  #  # itertools #  #  #  # # 

# There is also several combinatoric functions in itertool, such as product and permutation.
# These are used when you want to accomplish a task with all possible combinations of some items.

from itertools import product,permutations

letters = ("A","B")
print(list(product(letters,range(2))))
print(list(permutations(letters)))


# # # # # # # # # # # # # # # # # # # Classes

# We have previously looked at two paradigms of programming -imperative (using statements,loops,and functions as subroutines),and functional(using pure
# functions,higher-order functions,and recursion)
# 
# Another very popular paradigm is object-oriented programming(OOP). Objects are created using classes, which are actually the focal point of OOP.
# The class describes what the object will be,but is separate from the object itself.In other words , a class can be described as an object's blueprint
# ,description,or definition. You can use the same class as blueprint for creating multiple different objects.
# 
# Classes are created using the keyword class and an indented block,which contains class methods(which are functions).

class Cat:
    def __init__(self,color,legs):
        self.color = color
        self.legs = legs

felix = Cat('ginger',4)
rover = Cat('dog-colored',4)
stumpy = Cat('brown',3)


# The __init__ method is the most important method in a class. This is called when an instance(object) of the class is created,using the
# class name as a function
# All the methods must have self as their first parameter ,although it isn't explicitly passed.Python adds the self argument to the
# list for you; you do
# not need to include it when u call the methods. Within a method definition, self refers to the instance calling the method.Instances of
# a class have attributes , which are pieces of data associated with them. In this example,Cat instances have attributes color and legs.
# These can be accessed by putting a dot, and the attribute name after an instance.
# 
# In an __init__ method,self.attribute can therefore be used to set the initial value of an instance's attributes.

print(felix.color)

# Classes can have other methods defined to add funcctionality to them. Remember ,that all methods must have self as their first
# parameter . These methods are accessed using the same dot syntax as attributes.

class Dog:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def bark(self):
        print("Woof!!")
fido = Dog("Fido","brown")
print(fido.name)
fido.bark()

# Trying to access an attribute of an instance that isn't defined causes an AttributeError.  This also applies when you call and undefined
# method.
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height= height

rect = Rectangle(7,8)
# print(rect.color)

# # # # # # # # # # # # # # Inheritance

# Inheritance provides a way to share functionality between classes. Imagine several classes
# Cat,Dog,Rabbit and so on. Although they may differ in some ways (only Dog might have
# method bark),they are likely to be similar in others(all having the attributes color
# and name). This similarity can be expressed by making them all inherit from a superclass
# Animal, which contains the shared functionality.To inherit a class from another class,
# put the superclass name in parentheses after the class name.

class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
class Cat(Animal):
    def purr(self):
        print("purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!!")

fido = Dog('Fido','brown')
print(fido.color)
fido.bark()

