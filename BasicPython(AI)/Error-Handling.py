# Error handling
'''
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
try :
    print("Division is : ",a/b)
except Exception as e :
    print("some error occur!",e)

print("Thank you")
'''

# The try and except Block
'''
try:
    x = int("abc")
except:
    print("An error occurred")
'''   

# Handling Specific Errors
'''
try:
    x = int("abc")
except ValueError:
    print("Invalid conversion")
'''

# Multiple except Blocks
'''
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Division by zero is not allowed")
'''

# The else Block
'''
try:
    x = int("10")
except ValueError:
    print("Error")
else:
    print("Conversion successful")
'''

# The finally Block
'''
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution finished")
'''

# Raising Errors Manually
'''
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
'''

# Using pass in Error Handling
'''
try:
    x = int("abc")
except ValueError:
    pass
'''