from engine.worldmap import WorldMap
from random import randint, choice

def initial_item_populate(new_world):

    possible_items = ['a tree', 'a rock', 'a stream', 'a boot', 'some grass', 'some mushrooms', 'a cloud', 'crumpled paper', 'a fallen tree limb']
    north_limit = 1
    south_limit = -1
    east_limit = 1
    west_limit = -1
    lastitem = randint(1,7)
    x_list = []
    y_list = []

    #for x in range(west_limit - 1, east_limit + 1):
    #    x_list.append(x)

    #for y in range(south_limit - 1, north_limit + 1):
    #    y_list.append(y)

    x_list = list(range(west_limit, east_limit + 1))
    y_list = list(range(south_limit, north_limit + 1))

    for item in range(lastitem):
        new_world.AddItemAt(choice(x_list), choice(y_list), choice(possible_items))
