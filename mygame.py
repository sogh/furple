import random, sys, initialize

from engine.player import Player
from engine.simulation import Simulation
from engine.sunmoon import SunMoon
from engine.graphics import Graphics

class MyGame:
    def __init__(self):
        self.info_commands = ['help', 'info']
        self.player_move_commands = [
            'north', 'south', 'east', 'west',
            'n','s','e','w']
        self.fart_commands = ['fart']
        self.look_commands = ['look', 'search', 'investigate']
        self.npc_commands = ['greet']
        self.quit_commands = ['quit']

        self.all_commands = self.info_commands + self.player_move_commands + self.fart_commands + self.quit_commands + self.look_commands + self.npc_commands

        self.worldmap = initialize.GENERATE_PHEZYGG_WORLD()
        self.sim = Simulation()
        print("Beginning game...")
        self.player1 = Player()
        self.sim.AddUpdateable(self.player1)
        self.sun = SunMoon()
        self.sim.AddUpdateable(self.sun)
        initialize.initial_item_populate(self.worldmap)
        initialize.initial_npc_populate(self.worldmap)

        # Every game loop, add things to be rendered/printed to this list.
        self.render_list = []
        # Every game loop, update our input queue to process player input.
        # In normal operation, there will only be one entry in the queue. However, this
        # enables us to insert commands in the queue for testing purposes.
        self.input_queue = []

        self.graphics = Graphics()


    def run(self):
        # Main game loop
        while True:
            self.graphics.RenderText(f"Position: {self.player1.position.toString()}")
            self.graphics.RenderText("Move commands: n,s,e,w")
            self.graphics.RenderText(self.sun.toString())
            self.graphics.RenderText(self.worldmap.GetLocationDescription(self.player1.position.x, self.player1.position.y))
            self.graphics.RenderText(self.player1.PlayerStatus())
            
            # Every Loop execute one simulation tick.
            self.sim.Update()

            # Render all the graphics
            self.graphics.Render()

            # Take player input
            cmd = input("Enter command: ")
            lowcmd = cmd.lower()
            if lowcmd in self.player_move_commands:
                self.player1.move(lowcmd)
            elif lowcmd in self.info_commands:
                self.graphics.RenderText("All possible commands:")
                self.graphics.RenderText(self.all_commands)
            elif lowcmd in self.fart_commands:
                self.graphics.RenderText("You fart. It smells.")
            elif lowcmd in self.quit_commands:
                break
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


if __name__ == '__main__':
    game = MyGame()
    game.run()