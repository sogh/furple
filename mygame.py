import random

from engine.player import Player

print("Beginning game...")
player1 = Player()
print(f"You wake up to find yourself in the middle of dirt road, you walk straight for a few mins and see a fork in the road. Position: {player1.position.toString()}")
print("The left path is very foggy and you cannot see farther then a few feet")
print("The right path is blocked with thick vines but you might be able to squeeze in")

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
# player1.step(direction)
print(f"Position: {player1.position.toString()}")
if deadlypath == direction.lower():
    print("You hear a hissing sound, looks like you stepped on a snake's tail")
    print("The snake bites you and you die")
    print("Game over.")
else :
    print("Through sheer will, you managed to win.")
