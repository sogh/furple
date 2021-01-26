import random, sys, initialize
from collections import deque

from engine.player import Player
from engine.simulation import Simulation
from engine.sunmoon import SunMoon
from engine.graphics import Graphics

class MyGame:
    def __init__(self, worldmap=initialize.GENERATE_PHEZYGG_WORLD(), sim=Simulation(), player1=Player(), graphics=Graphics(), sun=SunMoon()):
        self.info_commands = ['help', 'info']
        self.player_move_commands = [
            'north', 'south', 'east', 'west',
            'n','s','e','w']
        self.fart_commands = ['fart']
        self.look_commands = ['look', 'search', 'investigate']
        self.npc_commands = ['greet']
        self.quit_commands = ['quit']

        self.all_commands = self.info_commands + self.player_move_commands + self.fart_commands + self.quit_commands + self.look_commands + self.npc_commands

        self.worldmap = worldmap
        self.sim = sim
        print("Beginning game...")
        self.player1 = player1
        self.sim.AddUpdateable(self.player1)
        self.sun = sun
        self.sim.AddUpdateable(self.sun)

        # Every game loop, add things to be rendered/printed to this list.
        self.render_list = []
        # Every game loop, update our input queue to process player input.
        # In normal operation, there will only be one entry in the queue. However, this
        # enables us to insert commands in the queue for testing purposes.
        self.input_queue = deque()

        self.graphics = graphics


    def Step(self):
        self.graphics.RenderText(f"Position: {self.player1.position.toString()}")
        self.graphics.RenderText("Move commands: n,s,e,w")
        self.graphics.RenderText(self.sun.toString())
        self.graphics.RenderText(self.worldmap.GetLocationDescription(self.player1.position.x, self.player1.position.y))
        self.graphics.RenderText(self.player1.PlayerStatus())
        
        # Every Loop execute one simulation tick.
        self.sim.Update()

        # Take player input
        if len(self.input_queue) > 0:
            cmd = self.input_queue.popleft()
        else:
            cmd = ''
        lowcmd = cmd.lower()
        if lowcmd in self.player_move_commands:
            self.player1.move(lowcmd)
        elif lowcmd in self.info_commands:
            self.graphics.RenderText("All possible commands:")
            self.graphics.RenderText(self.all_commands)
        elif lowcmd in self.fart_commands:
            self.graphics.RenderText("You fart. It smells.")
        elif lowcmd in self.quit_commands:
            return False
        elif lowcmd in self.look_commands:
            item_list_local = self.worldmap.GetItemDescriptions(self.player1.position.x, self.player1.position.y)
            for item in item_list_local:
                self.graphics.RenderText(f"You see {item}.")
            #npc_list_local = 
            for npc in self.worldmap.GetNPCDescriptions(self.player1.position.x, self.player1.position.y):
                self.graphics.RenderText(f"You see {npc.title()}.")
        elif lowcmd in self.npc_commands:
            for greeting in self.worldmap.greetnpcs(self.player1.position.x, self.player1.position.y):
                self.graphics.RenderText(greeting)
        else:
            self.graphics.RenderText(f"{cmd} is not a valid command.")
        
        # Render all the graphics
        self.graphics.Render()

        return True


    def Run(self):
        # Main game loop
        while self.Step():
            self.input_queue.append(input("Enter command: "))


if __name__ == '__main__':
    game = MyGame()
    game.Run()