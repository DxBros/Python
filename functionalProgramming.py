# Functional Programming
# is a type of programming based around functions
# A key part of functional programming is higher order functions
# Higher order functions take other functions as arguments or return them as results
def apply_twice(func,arg):
    return func(func(arg))

def add_five(x):
    return x+5
print(apply_twice(add_five,10))
# Answer is 20

# Functional Programming seeks to use pure functions .Pure functions have no side effects,and
# return a value that depends only on their arguments.
# This is how functions in math work:for example ,The cos(x) will,for the same value of x,always
# return the same result.
# Pure function :
def pure_function(x,y):
    temp = x +2*y
    return temp/(2*x+y)

#Impure function example

def impure(arg):
    some_list.append(arg)
    #The function is impure because it changed the state of the list

# Advantages of using pure functions are:
#     easier to reason about the test.
#     more efficient. Once the function has been evaluated
# for an input,the result can be stored
# and referred next time the function of that input
# is needed reducing the number of calls to the function
# This is called memoization
# disadvantage is they complicate otherwise an easy task

# # # # # lambda functions
# example simple squaring function
def some_func(f,arg):
    return f(arg)

print(some_func(lambda x:x**2,4))

# They are not much powerful they can only be used in simple situation
def polynomial(x):
    return x**2+5*x+4
print(polynomial(-4))

print((lambda x:x**2+5*x+4)(-4))

# They can be assigned to variables and used like normal functions.
double = lambda x:x*2
print(double(2))


