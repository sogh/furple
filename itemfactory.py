from engine.worldmap import WorldMap
from random import randint, choice

def initial_item_populate(new_world, north_limit = 1, south_limit = -1, east_limit = 1, west_limit = -1):
    possible_items = ['a tree', 'a rock', 'a stream', 'a boot', 'some grass', 'some mushrooms', 'a cloud', 'crumpled paper', 'a fallen tree limb']
    max_initial_items = 7

    for _ in range(randint(1,max_initial_items)):
        new_world.AddItemAt(choice(list(range(west_limit, east_limit + 1))), choice(list(range(south_limit, north_limit + 1))), choice(possible_items))