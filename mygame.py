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

# dict of dicts stores info for coordinates
player_location = {
    '(0,0)': {
        'location_name': 'start',
        'location_flavor': 'Its the start.',
    },
    '(0,1)': {
        'location_name': 'pforest',
        'location_flavor': 'Its a forest of penises, you need to get out of here, if only you could stop tripping ass-first.',
    },
    '(1,1)': {
        'location_name': 'forest',
        'location_flavor': 'Its a forest, you could see it better if not for all these damn trees.',
    },
    '(-1,1)': {
        'location_name': 'mforest',
        'location_flavor': 'Its a forest of mushrooms.',
    },
    '(1,0)': {
        'location_name': 'market',
        'location_flavor': 'An ancient market destroyed by nuclear fire, the diminutive shadows on the wall bring a tear to your eye.',
    },
    '(-1,0)': {
        'location_name': 'cave',
        'location_flavor': 'A deep cave.',
    },
    '(0,-1)': {
        'location_name': 'dessert',
        'location_flavor': 'An endless dessert, it looks delicious.',
    },
    '(1,-1)': {
        'location_name': 'desert',
        'location_flavor': 'Its a desert, the cake turns to sand in your mouth.',
    },
    '(-1,-1)': {
        'location_name': 'dessertdesert',
        'location_flavor': 'There seems to be nothing here.',
    },
}

while True:
    print(f"Position: {player1.position.toString()}")
    print("Move commands: n,s,e,w")
    # print(worldmap.GetLocationDescription(player1.position))
    if player1.position.toString() in player_location.keys():
        #prints the location flavor text if it exists
        current_location = player_location[player1.position.toString()]
        print(current_location['location_flavor'])
    else:
        print("Youre off the grid man!")
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
