# items = ("apple","banana","mango","orange")

# print(items)

# list_1 = list(items)
# print(list_1)

# numbers = (1, 2, 3)
# names = ("Alice", "Bob", "Charlie")
# mixed = (1, "Python", 3.5, True)

# single = (5,)

items = ("apple", "banana", "orange")

# accessing using index
print(items[0])
print(items[2])

print(items[-1])
print(items[-2])

# tuples length
print(len(items))

# Tuplr slicing
items = ("apple", "banana", "orange", "mango")

print(items[1:3])
print(items[:2])
print(items[2:])

#  Tuples immutable 
items = ("apple", "banana", "orange")
# items[1] = "grapes"    not values change
count = items.count("apple") 
print(count)

position = items.index("banana")
print(position)

# looping in tuples
items = ("apple", "banana", "orange")

for item in items:
    print(item)

# tuple packing
data = 10, 20, 30
print(data)
# tuple unpacking
a, b, c = data
print(a)
print(b)
print(c)

# convert list and tuple
items = ("apple", "banana")
items_list = list(items)

items_tuple = tuple(items_list)