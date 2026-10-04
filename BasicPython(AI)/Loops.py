# for loop

items = ["apple","banana","mango","orange"]

for item in items :
    print(item)

# using range with for loop

for i in range(10):
    print(i,end=" ")

print()

for i in range (10 , 50) :
    print(i,end=" ")


print()

for i in range (1,50,2):
    print(i,end=" ")

# Looping Through a String

name = "Anish Gupta"
print()
for char in name :
    print(char)

# The while Loop

count = 1 
while count < 20 :
    print(count)
    count += 1

# infinite Loop
# while True:
#     print("Running")


# Loop control statment
# break
for i in range (10):
    if i == 5:
        break
    print(i)
# continue
for i in range(5):
    if i == 2:
        continue
    print(i)
# pass
for i in range(5):
    pass

# nested loop
for i in range(3):
    for j in range(2):
        print(i, j)

# loop with else
for i in range(3):
    print(i)
else:
    print("Loop finished")