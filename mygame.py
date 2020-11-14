import random, sys

from engine.player import Player

info_commands = ['help', 'info']
player_move_commands = [
    'north', 'south', 'east', 'west',
    'n','s','e','w']
jester_commands = ['killjester', 'kill jester']
fart_commands = ['fart']

all_commands = info_commands + player_move_commands + jester_commands + fart_commands


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

while True:
    print(f"Position: {player1.position.toString()}")
    print("Move commands: n,s,e,w")
    # print(worldmap.GetLocationDescription(player1.position))
    cmd = input("Enter command :")
    lowcmd = cmd.lower()
    if lowcmd in player_move_commands:
        player1.move(lowcmd)
    elif lowcmd in jester_commands:
        dirs[lowcmd](lowcmd)
    elif lowcmd in info_commands:
        print("All possible commands:")
        print(all_commands)
    elif lowcmd in fart_commands:
        print("You fart. It smells.")
    else:
        print(f"{cmd} is not a valid command.")
