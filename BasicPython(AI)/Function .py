# default function
def greet():                #function make
    print("hello Anish")

greet()   #function call

# parameterise function
def greet(name):
    print("hello ",name)

greet("Aniush gupta")

# multiple parameters
def sum (a,b):
    print(a+b)

sum(2,4)

# return value
def add(x,y):
    return x+y

result = add(12,34)
print(result)

# Degfult parameter

def show (name =""):
    print("Hellow",name)

show()
show("Anish")

# keyword argument

def user_info (name , age):
    print(name,age)

user_info(age=21,name="Anish")


# Variable Length Arguments

def total(*args):
    print(args)

total(1,2,3,4,5,6)

# **kwargs
def user_details(**kwargs):
    print(kwargs)

user_details(name="Anish", age=21, course="BCA")

# Function Docstrings
def add(a, b):
    """Returns the sum of two numbers"""
    return a + b
print(add(2,3))

#Scope of variable
def test():
    x = 10
    print(x)

test()

# Function Inside a Function
def outer():
    def inner():
        print("Inside inner function")
    inner()

outer()
# inner()       error 

# lambda function

add = lambda a, b: a + b
print(add(3, 5))