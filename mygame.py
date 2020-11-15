import random, sys

from engine.player import Player
from mapfactory import GENERATE_PHEZYGG_WORLD

info_commands = ['help', 'info']
player_move_commands = [
    'north', 'south', 'east', 'west',
    'n','s','e','w']
fart_commands = ['fart']
quit_commands = ['quit']

all_commands = info_commands + player_move_commands + fart_commands + quit_commands

worldmap = GENERATE_PHEZYGG_WORLD()

print("Beginning game...")
player1 = Player()

# Main game loop

while True:
    print(f"Position: {player1.position.toString()}")
    print("Move commands: n,s,e,w")
    print(worldmap.GetLocationDescription(player1.position.x, player1.position.y))
    cmd = input("Enter command :")
    lowcmd = cmd.lower()
    if lowcmd in player_move_commands:
        player1.move(lowcmd)
    elif lowcmd in info_commands:
        print("All possible commands:")
        print(all_commands)
    elif lowcmd in fart_commands:
        print("You fart. It smells.")
    elif lowcmd in quit_commands:
        break
    else:
        print(f"{cmd} is not a valid command.")
