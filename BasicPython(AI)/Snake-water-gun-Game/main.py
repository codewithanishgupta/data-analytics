# Snake water gun game in python

import random

def get_win(computer , user):
    if user== computer:
        return None;

    # snake vs water
    if user=="s" and computer=="w":
        return True
    if user=="w" and computer=="s":
        return False
    
    # water vs gun
    if user == "w" and computer == "g":
        return True
    if user == "g" and computer == "w":
        return False
    
    # gun vs snake
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False


random_no = random.randint(1,3)
print("Coumputer turn : Snake(s) , Water(w) , Gun(g)")
if(random_no == 1):
    computer = "s"
elif(random_no == 2) :
    computer = "w"
else :
    computer = "g"

user = input("Your turn : Snake(s) , water(w) , Gun(g) : ").lower()

result = get_win(computer , user)
print("computer turn : ",computer)
print("Your turn :" , user)
if result is None:
    print("It's Draw!")
elif(result == True):
    print("You win!")
else :
    print("You lose!")