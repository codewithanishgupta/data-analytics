items = {"Java programing","Python","C Programming","C++ Programming"}

# empty = set();  this is empty set
# empty = {}      Error

# print type and length
'''
 print(type(items))
 print(items[2])  error
 print(len(items))
'''

# print(items)
# items.update(["Web-Dev","Data Analytics"])
# print(items)

# items.remove("C Programming")
# # items.discard("C program")    remove element when it find and other than skeep
# print(items)

# for item in items:
#     print(item)


# items.add("English")
# print(items)

# a = items.pop()
# print(items,"\n",a)

# items.clear()
# print(items)

a = {1,2,3,4,5}
b = {3,4,5,6,7,8,9}

print(a.union(b))
print(b.union(a)) # same as a.union(b)
result = a.intersection(b)
print(result)

print(a.difference(b)) 
print(b.difference(a)) # diffrent as a.diffrenence(b)

print(a.symmetric_difference(b))


print(5 in a)
print(6 in a)