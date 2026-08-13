#imports
from Room import room
from Item import item

#generate rooms
gate = room("gate")
gate.set_description("A large gold gate closing off the manor")
front_room = room("Front Room")
front_room.set_description("The room is dimly lit with red carpet and a large central donut shaped wooden desk")
secrity_office = room("Secrity Office")
secrity_office.set_description("The secrity office is dark with all its light comming from the large video camera ")
dinning_room = room("Dinning Room")
dinning_room.set_description("")
kitchen = room("Kitchen")
kitchen.set_description("")
wine_celler = room("Wine Celler")
wine_celler.set_description("")
low_hall = room("Lower Hallway")
low_hall.set_description("")
up_hall = room("Upper Hallway")
up_hall.set_description("")
storage = room("Storage Room")
storage.set_description("")
library = room("Library")
library.set_description("")
office = room("Office")
office.set_description("")
g_low_hall = room("Lower Garden Hallway")
g_low_hall.set_description("")
g_up_hall = room("Upper Garden Hallway")
g_up_hall.set_description("")
g_storage = room("Garden Storage")
g_storage.set_description("")
garden = room("Garden")
garden.set_description("")
art_room = room("")
art_room.set_description("")
stage_room = room("")
stage_room.set_description("")
meeting_room = room("")
meeting_room.set_description("")
head_office = room("")
head_office.set_description("")

    #Room links
gate.link_cave(front_room, "north")
front_room.link_cave(gate, "south")
front_room.link_cave(secrity_office, "east")
secrity_office.link_cave(front_room, "west")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")
#.link_cave(, "")

#item code
vegemite = item("vegemite")
vegemite.set_description("yummy vegemite great placeholder item")
gate.set_item(vegemite)



#start code

bag = []
current_cave = gate
dead = False


while dead == False: # game loop — runs until win or death
    current_cave.get_details()
    item = current_cave.get_item()
    if item is not None:
        item.describe()

    command = input(">")

    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_cave.set_item(None)