#Exception handling in python

#Various errors
# ImportError: a import fails
# IndexError : a list is indexed with an out-of-range number
# NameError : an unknown variable is used
# SyntaxError : the code can't be parsed properly
# TypeError : a function is called on a value of an inappropriate type
# ValueError : a function is called on a value of the correct type , but with an inappropriate
# value

# # # # # # Try and except blocks

# try:
#     a =int(input())
#     b=int(input())
#     print(a/b)
# except Exception as e:
#     print(e)

#######   finally and raise
# try:
#     a =int(input())
#     b=input()
#     print(a/b)
# except:
#     print("TypeError")
#     print(x)#even when exception in exception occurs still finally will run
#     raise #reraises the error occured
# finally:
#     print("This will definitely run\n")
    
# name ="adarsh"
# raise NameError("Invalid Name") # an error can be simply raised with better details

#######   Assertions
# assertion is a sanity check you can turn on and off when you have finished testing the
# program
# print(1)
# assert 1+2  == 3
# print(2)
# assert (1+2 == 4),"how dumb to check 1+2 == 4"
# print(3)
# AssertionError is raised
# 
##### File handling
# + - means extra access r+ means read  and write both
# r - means read mode
# w - means write mode
# a - means append mode
# b - means binary mode

myfile = open("adarsh.txt",'w')#used to open already existing file else FileNotFoundError will be raised
bytes =myfile.write("hello today it is sunny day ")
print(bytes)#write method returns the size of file written
myfile.close()

# when a file is opened in write mode its existing contents are deleted
with open("adarsh.txt","r+") as f:
    cont = f.read()
    print(cont)
