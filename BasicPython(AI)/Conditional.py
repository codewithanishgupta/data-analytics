# Conditinal Statment Practice 

age = 18 ;

# If statment
if(age>=18):
    print("Adult")

# if-else statment

age = 16

if age>=18 :
    print("Adult")
else :
    print("Not Adult")

# elif statment(use to check multiple condition check)

marks = 60;

if marks>=80 and marks<=100 :
    print("Grade : A")
elif marks>=60 and marks <80 :
    print("Grade : B")
elif marks >= 40 and marks < 60 : 
    print("Grade : C")
elif marks >= 30 and marks < 40 :
    print("Grade : D")
else :
    print("Fail")


# indentation in conditionals

if True :
    print("This is run ")
    print("This is also run ")


# Comparison Operators in Conditions

a = 110

if (a==10) :
    print("Equal")

if (a!=10) :
    print("Not equal")

# Logical Operators in Conditions

age = 25
country = "India"

if age >= 18 and country == "India":
    print("Allowed")

# Nested Conditionals

age = 20

if age >= 18:
    if age < 60:
        print("Adult")

# Using pass in Conditionals
age = 15

if age >= 18:
    pass
else:
    print("Minor")

# Conditional Expressions (Ternary Operator)

age = 20
status = "Adult" if age >= 18 else "Minor"