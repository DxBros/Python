# A class that inherits from another class is called a subclass. A class that is inherited from is called a superclass.If a class inherits from another
# with the same attributes or methods ,it overrides them.

class Wolf:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def bark(self):
        print("Grr...")
    
def Dog(Wolf):
    def bark(self):
        print("Woof!")

husky = Dog("Max","grey")
husky.bark()

        
# Inheritance can also be indirect .One class can inherit from another,and that class can inherit from third class.

class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")
class C(B):
    def third_method(self):
        print("C method")

c =C()
c.method()
c.another_method()
c.third_method()

# The function super is a useful inheritance-related function that refers to the parent class.
# It can be used to find the method with a certain name in an object's superclass.

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

# Magic methods are special methods which have double underscores at the beginning and end of their names.
# They are also known as dunders .So far ,the only one we have encountered is __init__ , but there are several others. They are used to create
# functionality that can't be represened as normal method. One common use of them is operator overloading. This means defining operators for custom
# classes that allow operators such as + and * to be used on them.
# An example magic method is __add__ for +.

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)

first = Vector2D(5,7)
second = Vector2D(8,9)
res = first + second
print(res.x)
print(res.y)

# More magic methods for common operators:
#     __sub__ , __mul__,__div__,__truediv__,__floordiv__,__mod__,__pow__,__and__,__xor__,__or__

# The expression x+y is translated to x.__add__(y). However ,if x hasn't implemented __add__,and x and y are of different types, then y.__radd__(x) is
# called .There are equivalent r methods for all magic methods just mentioned.

class SpecialString:
    def __init__(self,cont):
        self.cont = cont
    
    def __truediv__(self,other):
        line = "="*len(other.cont)
        return "\n".join([self.cont,line,other.cont])
spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam/hello)

# Python also provides magic methods for comparison.
# __lt__ for < ,__le__ for <= ,__eq__ for ==,__ne__ for !=,__gt__ for >,__ge__ for >=

# if __ne__ is not implemented it returns opposite of __eq__.There is no other relationship
# between the other operators.

class SpecialString:
    def __init__(self,cont):
        self.cont = cont
    
    def __gt__(self,other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index]+">"+self.cont
            result +=">"+ other.cont[index:]
            print(result)
spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam>eggs


