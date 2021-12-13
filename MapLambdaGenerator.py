# # # map,filter,generator's,yield
# the built in functions map and filter are very useful higher-order functions that operate
# on lists(or similar objects called iterables).
# The function map takes a function and an iterable as arguments,
# and returns a new iterable with the function applied to each argument.

def add_five(x):
    return x+5

nums = [11,22,33,44,55]
result  = list(map(add_five,nums))
print(result)

# we can use lambda function
num = [1,2,3,4,5]
result = list(map(lambda x:5*x,num))
print(result)


num1 = [1,2,3,4,5,6,7,8]
result1 = list(filter(lambda x:x%2==0,num1))
print(result1)

# generators are a type of iterable,like  lists or  tuples. Unlike lists, they don't aallow indexing
# with arbitrary indices, but they can still be iterated through with for loops.
# They can be created using funcitons and the yield statement.

def countdown():
    i=5
    while i>0:
        yield i
        i -= 1

for i in countdown():
    print(i)

def infinite_sevens():
    while True:
        yield 7

# for i in infinite_sevens():
#     print(i)

# generators allow you to declare a function that
# behaves like an iterator,i.e. it can be used
# in for loop.

def numbers(x):
    for i in range(x):
        if i%2 == 0:
            yield i
            
print(list(numbers(11)))

