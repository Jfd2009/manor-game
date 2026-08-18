class room :
     def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.item = None

     def set_description(self, room_description) :
         self.description = room_description

     def get_description(self):
         return self.description

     def set_name(self, room_name):
         self.name = room_name

     def get_name(self):
         return self.name

     #[placeholder]

     def link_room(self, room_to_link, direction): 
        self.linked_rooms[direction] = room_to_link    

     def get_details(self):
        print(self.name)
        print('----------')
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("[The " + room.get_name() + " is " + direction + "]")
            
     def move(self, direction): 

        if direction in self.linked_rooms: 

            return self.linked_rooms[direction] 

        else: 

            print("You slam your head into a wall") 

            return self 
     def set_item(self, new_item):   
        self.item = new_item

     def get_item(self):
        return self.item
    