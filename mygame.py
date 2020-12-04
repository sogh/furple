import random, sys

from engine.player import Player
from engine.simulation import Simulation
from engine.sunmoon import SunMoon
from mapfactory import GENERATE_PHEZYGG_WORLD

info_commands = ['help', 'info']
player_move_commands = [
    'north', 'south', 'east', 'west',
    'n','s','e','w']
fart_commands = ['fart']
look_commands = ['look', 'search', 'investigate']
quit_commands = ['quit']

all_commands = info_commands + player_move_commands + fart_commands + quit_commands + look_commands

worldmap = GENERATE_PHEZYGG_WORLD()
sim = Simulation()
print("Beginning game...")
player1 = Player()
sim.AddUpdateable(player1)
sun = SunMoon()
sim.AddUpdateable(sun)

# Every game loop, add things to be rendered/printed to this list.
render_list = []
# Main game loop
while True:
    render_list.append(f"Position: {player1.position.toString()}")
    render_list.append("Move commands: n,s,e,w")
    render_list.append(sun.toString())
    render_list.append(worldmap.GetLocationDescription(player1.position.x, player1.position.y))
    render_list.append(player1.PlayerStatus())
    
    for r in render_list:
        # Fancy renderer, ray tracing coming soon.
        print(r)
    render_list = []        
    
    # Every Loop execute one simulation tick.
    sim.Update()

    # Take player input
    cmd = input("Enter command: ")
    lowcmd = cmd.lower()
    if lowcmd in player_move_commands:
        player1.move(lowcmd)
    elif lowcmd in info_commands:
        render_list.append("All possible commands:")
        render_list.append(all_commands)
    elif lowcmd in fart_commands:
        render_list.append("You fart. It smells.")
    elif lowcmd in quit_commands:
        break
    elif lowcmd in look_commands:
        item_list_local = worldmap.GetItemDescriptions(player1.position.x,player1.position.y)
        for item in item_list_local:
            render_list.append(f"You see a {item}.")
    else:
        render_list.append(f"{cmd} is not a valid command.")
