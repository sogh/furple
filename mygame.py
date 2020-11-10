import random, sys

from engine.player import Player

print("Beginning game...")
player1 = Player()
print(f"You wake up to find yourself in the middle of dirt road, you walk straight for a few mins and see a fork in the road. Position: {player1.position.toString()}")
print("The left path is very foggy and you cannot see farther then a few feet")
print("The right path is blocked with thick vines but you might be able to squeeze in")

def deadlypath(lowdir):
    print(f"you went {lowdir}")
    print("You hear a hissing sound, looks like you stepped on a snake's tail")
    print("The snake bites you and you die")
    print("Game over.")
    sys.exit()

def winpath(lowdir):
    print(f"you went {lowdir}")
    print("Through sheer will, you managed to win.")
    sys.exit()

killjester_really = False
def killjester(lowdir):
    global killjester_really
    if not killjester_really:
        print("Jingle is our friend.  She is here to help us.")
        killjester_really = True
    else:
        print("Jingle is dead.")
        print("Game over.")
        print("Let's take another call.")
        sys.exit()

dirs = {
    "kill jester": killjester,
    "killjester": killjester,
}
if random.randint(1,2) == 1 :
    dirs["left"] = deadlypath
    dirs["right"] = winpath
else :
    dirs["right"] = deadlypath
    dirs["left"] = winpath

while True:
    direction = input("Do you want to go left or right? :")
    lowdir = direction.lower()
    if lowdir in dirs:
        dirs[lowdir](lowdir)
    else:
        print(f"{direction} is not a direction you can go to, please choose left or right")
