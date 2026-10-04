
text = "Anish Gupta"
# multi line text
multi = '''Hi, I am Anish Gupta,a BCA student
        I am passionate about C,C++,Java,Python,Web Development, and learning new technologies.

        I enjoy solving problems,practicing coading.
        My favorite programing language is Java.
'''

print(multi)

print(len(text))
print(text[0])
print(text[1])
print(text[3])

print(text[0:5])
print(text[6:])
print(text[3:6])

print(text[-3:])
print(text[:-6])
print(text[-6:-2])


print(text)
print(multi)
print(text.lower())
print(text.upper())
print(text.split())
print(text.strip())
print(text.replace("Gupta", "Prabhakar"))

text = "apple,banana,orange"
items = text.split(",")
print(items)

items = ["apple", "banana", "orange"]
text = ",".join(items)
print(text)

email = "test@gmail.com"
print(email.startswith("test"))
print(email.endswith(".com"))

name = input("Whats your name : ")
age = input("What is your age : ")
city = input("Where is your city : ")

print("Name : "+name+" Age : "+age+" city : "+city)

print(f"Nmae is : {name} Age is : {age} city is : {city}")

text = "Python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())

