# creat dectionaries

'''
student = {
    "name" : "Anish Gupta",
    "roll" : "29",
    "course" : "BCA",
    "city" : "Bihar",
    "collage" : "MPSsc"
}
print(student)
print(type(student))
'''

# in other way to creat

student = dict(name ="Anish",age = 21, city = "Muzaffarpur")

print(student)
print(type(student))

# Accessing dictionary value
print(student["name"])
print(student["age"])

# using get method
print(student.get("city"))
print(student.get("name"))

# Adding and updating values
student["city"]="Bihar" # update city name
student["course"]="BCA" # add values
print(student)

# Removing Dictionary
student.pop("course")
print(student)

#  Remove last update value
student.popitem()
print(student)

# Delete value
del student["age"]
print(student)

# clear all
student.clear()
print(student)


# new dictionary creat
employee = {
    "name": "Anish ",
    "age" : 29,
    "work": "Data Analytics"
}

print(employee)

# directories key, values and items
print(employee.keys())
print(employee.values())
print(employee.items())

# Looping through a dictionary
for key in employee:                    # looping through key
    print(key)

for value in employee.values():         # looping through value
    print(value)

for key,value in employee.items():      # looping through key and value pairs
    print(key,value)


# Checking for keys
print("name" in employee)

# copy dictionary
new_employee = employee.copy()
print(new_employee)

#  Updating Dictionary
employee.update({
    "name": "Ganga kumar",
    "age": 22
})
print(employee)

# Nested Dictionary

user = {
    "id": 1,
    "profile":{
        "name":"Anish",
        "email":"anish123@gmail.com"
    }
}

print(user)
print(user["profile"]["email"])