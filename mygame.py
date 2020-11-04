import random

print("Beginning game...")
print("You wake up to find yourself in the middle of dirt road, you walk straight for a few mins and see a fork in the road.")
print("The left path is very foggy and you cannot see father then a few feet")
print("The right path is blocked with thick veins but you might be able to sqeeze in")

if random.randint(1,2) == 1 :
    deadlypath = "left"
else :
    deadlypath = "right"
    
while True:
    direction = input("Do you want to go left or right? :")
    if direction.lower() == "left" :
        print("you went left")
        break
    elif direction.lower() == "right" :
        print("you went right")
        break
    else :
        print(f"{direction} is not a direction you can go to, please choose left or right")

if deadlypath == direction.lower():
    print(f"You go {direction} and hear a hissing sound, looks like you stepped on a snake's tail")
    print("The snake bites you and you die")
    print("Game over.")
else :
    print("Through sheer will, you managed to win.")
