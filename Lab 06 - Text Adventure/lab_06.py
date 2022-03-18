#Lab 6 Text Adventure Due 3/17/2022

print('\nWelcome To The Adventure Game Room')

# 1 Define a class called Room
class Room:
    room = []
    def __init__(self, description , north, east, west, south):
        self.room.append(description)
        self.room.append(north)
        self.room.append(east)
        self.room.append(west)
        self.room.append(south)

    def get_description(self):
        return self.room[0]
    def get_north(self):
        return self.room[1]
    def get_east(self):
        return self.room[2]
    def get_west(self):
        return self.room[3]
    def get_south(self):
        return self.room[4]

    # create Character
    class Character():
        def __init__(self, name, description , room ):
            self.name = name
            self.description = description
            self.room = room

    room_list = []
    # List all the room you need
    #              Main Gate
    # Bed Room    North hall       Office
    # Library    South Hall      Dining Room
    room = ["You are in Library, \nThere is a passage to the North,and East.", 3, None, None, 1]
    room_list.append(room)
    room = ["You are in South Hall, \nThere is a passage to the North, East.", 4, None, 0, 2]
    room_list.append(room)
    room = ["You are in Dining Room,\nThere is a passage to the North, and West.", 5, None, None, 1]
    room_list.append(room)
    room = ["You are in Bedroom,\nThere is a passage to the East, and South.", None, 0, 4, None]
    room_list.append(room)
    room = ["You are in North Hall,\nThere is a passage to the  North, East , West, and South.", 6, 1, 5, 3]
    room_list.append(room)
    room = ["You are in Office,\nThere is a passage to the West,  and South.", None, 2, None, 4]
    room_list.append(room)
    room = ["You are in Main Gate,\nThere is a passage to the  South.", None, 4, None, None]
    room_list.append(room)

    #  Current room  0 initially
    current_room = 0
    #  Print the room_list variable
    for rooms in room_list:
        print(rooms)

        #  first room element zero
        print(room_list[0])
        print("\n")

        #  print current room now
        print(room_list[current_room])
        print("\n")

        #  print current room decription
        print(room_list[current_room].get_description())
        print("\n")

    # Create a variable done and set it to false
    done = False
    while not done:
        #  print a blank line
        print(room_list[int(current_room)][0])

        #  print current room decription
        print("Which direction you want to go : north, south, east or west?")
        print("Enter q or quit if you want to  quit the game: ")

        #  if a player want to go north
        if player_choice == "north" or "n":
            next_room = room_list[current_room].get_north()
            # 15 create next room = none
            if next_room is None:
                print("there's no door for you to go through ")
            else:
                current_room = next_room

        #  test if player can go to new room
        # Add elif statements to handle east, south, and west.
        elif player_choice == "east" or "e":
            next_room = room_list[current_room].get_east()
            if next_room is None:
                print("there's no door for you to go through ")
            else:
                current_room = next_room

        elif player_choice == "south" or "e":
            next_room =  room_list[current_room].get_south()
            if next_room is None:
                print("there's no door for you to go through ")
            else:
                current_room = next_room

        elif player_choice == "west" or "w":
            next_room = room_list[current_room].get_west()
            if next_room is None:
                print("there's no door for you to go through ")
            else:
                current_room = next_room

        # Option if a player want to quit the game
        elif player_choice == "quit" or "q":
            done = True

        else:
            print("The direction is not clear. Please try again .")


