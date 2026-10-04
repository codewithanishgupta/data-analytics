# file write 
''' 
a="Anish is the good boy. And he is very innocent "
file = open("anish.txt","w")
file.write(a)
'''
# File read
'''
file=open("aboutme.txt","r")
content = file.read()
print(content)

# read one line only
file = open("anish.txt","r")
line = file.readline()
print(line)

# read all lines (it is print as a list)
file = open("anish.txt", "r")
lines = file.readlines()
print(lines)
'''

# using with(The with statement automatically closes the file. )
'''
x="Hyyy everyone, How are you"
with open("anish.txt","w") as file:
    file.write(x)
'''

# Using append
'''
file=open("anish.txt","a")
file.write("\n New line added")
'''
# write multiple lines
'''
lines = ["Line-1 \n","Line-2 \n","Line-3 \n"]

with open("anish.txt","w") as file :
    file.writelines(lines)
'''

#Checking File Existence
'''
import os
if os.path.exists("anish.txt"):
    print("File Exists")
'''

# Reading and Writing Binary Files
'''
with open("image.png", "rb") as file:
    data = file.read()

with open("copy.png", "wb") as file:
    file.write(data)
'''
# file.close()