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
gate.link_room(front_room, "north")
front_room.link_room(gate, "south")
front_room.link_room(secrity_office, "east")
front_room.link_room(low_hall, "north")
front_room.link_room(dinning_room, "west")
secrity_office.link_room(front_room, "west")
dinning_room.link_room(front_room, "east")
dinning_room.link_room(kitchen, "west")
low_hall.link_room(up_hall, "north")
low_hall.link_room(storage, "east")
low_hall.link_room(front_room, "south")
low_hall.link_room(garden, "west")
storage.link_room(low_hall, "west")
garden.link_room(low_hall, "east")
garden.link_room(g_up_hall, "north")
garden.link_room(kitchen, "south")
kitchen.link_room(dinning_room, "east")
kitchen.link_room(garden, "north")
kitchen.link_room(wine_celler, "west")
wine_celler.link_room(kitchen, "east")
up_hall.link_room(art_room, "north")
up_hall.link_room(library, "east")
up_hall.link_room(low_hall, "south")
up_hall.link_room(g_low_hall, "west")
library.link_room

office.link_room

g_low_hall.link_room(up_hall, "east")
g_low_hall.link_room(g_up_hall, "west")
g_up_hall.link_room(meeting_room, "north")
g_up_hall.link_room(g_low_hall, "east")
g_up_hall.link_room(garden, "south")
g_up_hall.link_room(g_storage, "west")
g_storage.link_room(g_up_hall, "east")
#.link_room(, "")
#.link_room(, "")
#.link_room(, "")
#.link_room(, "")


#item code
vegemite = item("vegemite")
vegemite.set_description("yummy vegemite great placeholder item")
gate.set_item(vegemite)



#start code

bag = []
current_room = gate
dead = False


while dead == False: # game loop — runs until win or death
    current_room.get_details()
    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input(">")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_room.set_item(None)