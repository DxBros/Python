# # # # # # # # # # # # # # # # # # # # # # # # # MAGIC METHODS
# __len__ for len(),__getitem__ for indexing,__setitem__ for assigning to indexed values,__delitem__ for deleting indexed values,__iter__ for iteration
# over objects (e.g.,in for loops),__contains__ for in
# There are many other magic methods that we won't cover  here,such as __call__ for calling objects as functions ,and __init__ ,__str__,and the like,for
# converting objects to built-in types.
import random

class VagueList:
    def __init__(self,cont):
        self.cont = cont
    
    def __getitem__(self,index):
        return self.cont[index +random.randint(-1,1)]
    
    def __len__(self):
        return random.randint(0,len(self.cont)*2)

vague_list = VagueList(["A","B","C","D","E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

# We have overridden the len() function for the class VagueList to return a random number. The indexing function also returns a random item in a range
# from the list,based on the expression.

###########################################Object lifecycle
# The lifecycle of an object is made up of its creation,manipulation,and destruction.
# The first stage of the life-cycle of an object is the definition of the class to which it belongs.
# The next stage is the instantiation of an instance, when __init__ is called. Memory is allocated to store the instance.Just before this occurs,the
# __new__ method of the class is called. This usually is overriden only in special cases.

# After this has happened ,the object is ready to be used.Other code can then interact with the object ,by calling functions on it and accessing its
# attributes. Eventually ,it will finish being used, and  can be destroyed.

# When an object is destroyed ,the memory allocated to it is freed up,and can be used for other purposes.
# Destruction of an object occurs when its reference count reaches zero.Reference count is the number of variables or other elements that refer to an
# object .If nothing is referring to it (it has a reference count of zero) nothing can interact with it,so it can be safely deleted.
# In some situations,two(or more) objects can be referred to by each other only,and therefore can be deleted as well.
# The del statement reduces the reference count of an object by one ,and this often leads to its deletion. The magic method for the del
# statement is __del__. The process of deleting objects when they are no longer needed is called garbage collection.
# In summary ,an object's reference count increases when it is assigned a new name or placed in a container (list,tuple,or dictionary).The object's
# reference count decreases then it's deleted with del,its reference s reassigned ,or its reference goes out of scope. When an object's reference count
# reaches zero,Python automatically deletes it.

a = 42
b = a
c =[a]

del a
b= 100
c[0]=-1


###################################### Data Hiding
# A key part of object-oriented programming is encapsulation,which involves packaging of related variables and functions into a single easy-to-use object
# - an instance of a class. A related concept is data hiding ,which stated that implementation details of a class should be hidden ,and a clean standard
# interface be presented for those who want ot use the class.
# 
# The Python philosophy is slightly different .It is often statd a "we are all consenting adult's here",meaning that you shouldn't put arbitrary restrictions
# on accessing parts of a class.Hence there are no ways of enforcing a method or attribute be strictly private.

# Weakly private methods and attributes have a single underscore at the beginning .This signals that they are private, and shouldn't be used by external
# code .However,it is mostly only convention,and does not stop external code from accessing them.Its only actual effect is that from module_name import *
# won't import variables that start with a single underscore.

class Queue:
    def __init__(self,contents):
        self._hiddenlist = list(contents)
    
    def push(self,value):
        self._hiddenlist.insert(0,value)
    
    def pop(self):
        return self._hiddenlist.pop(-1)
    
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue= Queue([1,2,3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

# Strongly private methods and attributes have a double underscore at the beginning of their names.This causes their names to mangles,which means that
# they can't be accessed from outside the class.
# The purpose of this isn't to ensure that they are private but to avoid bugs if there are subclasses that have methods or attributes with the same
# names.
# Name mangled methods can still be accessed externally ,but by a different name. The method _privatemethod of class Spam could be accessed externally with
# _Spam_privatemethod.

class Spam:
    __egg=7
    def print_egg(self):
        print(self.__egg)
    
s =Spam()
s.print_egg()
print(s._Spam__egg)
# print(s.__egg)

# Class Methods
# Methods of objects we've looked at so far are called by an instance of a class,which is then passed to the self parameter of the method.Class methods
# are different -they are called by a class, which is passed to the cls parameter of the method. A common use for these are factory methods,which
# instantiate an instance of a class ,using different parameters than those usually passed to the class constructor. Class methods are marked with a
# classmethod decorator.

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width*self.height
    
    @classmethod
    def new_square(cls,side_length):
        return cls(side_length,side_length)

square  = Rectangle.new_square(5)
print(square.calculate_area())

# new_square is a class method and is called on the class,rather than on an instance of the
# class .It returns a new object of the class cls.

# Static methods ae similar to class methods,except they don't receive any additional
# arguments ;that are identical to normal functions that belong to a class. They are
# marked with the staticmethod decorator.

class Pizza:
    def __init__(self,toppings):
        self.toppings = toppings
    
    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No Pineapples!")
        else:
            return True

ingredients= ["cheese","onions","spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
    
