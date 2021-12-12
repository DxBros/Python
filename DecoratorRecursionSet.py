# Decorator's provide a way to modify functions using other functions.
# This is ideal when you need to extend the function functionality of  functions that you don't want to modify

def decor(func):
    def wrap():
        print("Hello This is a decorator....")
        func()
        print("Hello This is a decorator....")
    return wrap

def func():
    print("My name is Adarsh which is going to be encapsulated in the text of decorator's")

decorated = decor(func)
# Then simply decorated can be called

@decor
def myfunc():
    print("This is a shortcut to use decorator....")

# In this case I have changed the previous function wrap() is replaced with return wrap
myfunc()


# # # # # # # # # # # # # # # RECURSION
# Recursion is a very important concept in fundamental programming. The fundamental part of recursion
# is self-reference-functions calling themselves. It is used to solve problems that can
# be broken up into eaiser sub-problems of the same type.

# A classic example of a function that is implemented recursively is the factorial function.
# which finds the product of all positive integers below a specified number.For example,5!
# is 5 x 4 x 3 x 2 x 1 --> 5*factorial(4)----> 5*4*factorial(3)--->5*4*3*2*1*factorial(0) and we
# know that factorial of 0 is 1.this condition is known as the base case and is the heart of recursion

# def factorial(x):
#     if(x==0):
#         return 1
#     return x*factorial(x-1)
# print(factorial(5))

# Recurison can also be indirect . One fucntion can call a second, which calls the first,
# ,which calls the second and so on. This can occur with any number of functions.
# 
def is_even(x):
    if x==0:
        return True
    return is_odd(x-1)
def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))
# 
# logic for is_odd(1)---> is_odd(1)->!(is_even(1)->(is_odd(0)->!(is_even(0)->True)->False->False->True)

# # # # # # # # # # # # # # # SETS

# Sets are data structures,similar to lists or dictionaries. They are created using curly braces
# ,or the set function. They share some functionality with lists, such as the use of int to check whether
# they contain a particular item.

num_set = {1,2,3,4,5}
word_set = set(['spam','eggs','sausage'])
print(3 in num_set)
print('spam' not in word_set)

# Sets differ from lists in several ways, but share several list operations such as len.
# They are unordered, which means that they can't be indexed. They cannot contain duplicate
# elements. Due to the way they are stored ,it's faster to check whether an item is part of a
# set ,rather than part of list.
# Insted of using append to add to a setuse add.
# The method remove removes a specific element from a set
# PoP remobes an arbitrary element.

nums = {1,2,9,10,3,4,5,6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

# Basically sets can be used for membership testing and elimination of duplicates.
# We can use set methods (from Maths) in these sets
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 & set2)# Intersection
print(set1 | set2)# Union
print(set1 ^ set2)# Symmertric Difference
print(set1 - set2)# Difference
print(set2 - set1)# Difference

