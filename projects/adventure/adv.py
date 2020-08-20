import math
from room import Room
from player import Player
from world import World
import random
from ast import literal_eval


class Player:

    def __init__(self, starting_room):
        self.current_room = starting_room

    def travel(self, direction, show_rooms=False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")


class World:
    def __init__(self):
        self.starting_room = None
        self.rooms = {}
        self.room_grid = []
        self.grid_size = 0

    def load_graph(self, room_graph):
        num_rooms = len(room_graph)
        rooms = [None] * num_rooms
        grid_size = 1
        for i in range(0, num_rooms):
            x = room_graph[i][0][0]
            grid_size = max(
                grid_size, room_graph[i][0][0], room_graph[i][0][1])
            self.rooms[i] = Room(
                f"Room {i}", f"({room_graph[i][0][0]},{room_graph[i][0][1]})", i, room_graph[i][0][0], room_graph[i][0][1])
        self.room_grid = []
        grid_size += 1
        self.grid_size = grid_size
        for i in range(0, grid_size):
            self.room_grid.append([None] * grid_size)
        for room_id in room_graph:
            room = self.rooms[room_id]
            self.room_grid[room.x][room.y] = room
            if 'n' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms(
                    'n', self.rooms[room_graph[room_id][1]['n']])
            if 's' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms(
                    's', self.rooms[room_graph[room_id][1]['s']])
            if 'e' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms(
                    'e', self.rooms[room_graph[room_id][1]['e']])
            if 'w' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms(
                    'w', self.rooms[room_graph[room_id][1]['w']])
        self.starting_room = self.rooms[0]

    def print_rooms(self):
        rotated_room_grid = []
        for i in range(0, len(self.room_grid)):
            rotated_room_grid.append([None] * len(self.room_grid))
        for i in range(len(self.room_grid)):
            for j in range(len(self.room_grid[0])):
                rotated_room_grid[len(self.room_grid[0]) -
                                  j - 1][i] = self.room_grid[i][j]
        print("#####")
        str = ""
        for row in rotated_room_grid:
            all_null = True
            for room in row:
                if room is not None:
                    all_null = False
                    break
            if all_null:
                continue
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
        print(str)
        print("#####")

# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, id=0, x=None, y=None):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.get_exits_string()}\n"

    def print_room_description(self, player):
        print(str(self))

    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits

    def get_exits_string(self):
        return f"Exits: [{', '.join(self.get_exits())}]"

    def connect_rooms(self, direction, connecting_room):
        if direction == "n":
            self.n_to = connecting_room
            connecting_room.s_to = self
        elif direction == "s":
            self.s_to = connecting_room
            connecting_room.n_to = self
        elif direction == "e":
            self.e_to = connecting_room
            connecting_room.w_to = self
        elif direction == "w":
            self.w_to = connecting_room
            connecting_room.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None

    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def get_coords(self):
        return [self.x, self.y]


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def traverse(world, traversal_path):
    initial = 0
    s = Stack()
    visited = {0: {}}
    reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    # movements = []
    # while visited has value and has rooms

    def new_move(visited, current_room):
        exits = visited[current_room.id]
        for directions in exits:
            if exits[directions] == '?' and current_room.get_room_in_direction(directions).id not in visited:
                return directions
        return None

    def new_room(traversal_path, visited, current_room, s, reverse):
        while True:
            remove = s.pop()
            traversal_path.append(remove)
            next_room = current_room.get_room_in_direction(remove)
            if "?" in visited[next_room.id].values():
                return next_room
            current_room = next_room

    while len(visited) < len(world.rooms):

        # initiate current_room
        current_room = world.rooms[initial]

        # print(current_room)

        # if current room is not in visited then set it to ?
        if current_room not in visited:
            # 0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
            for direction in current_room.get_exits():
                visited[current_room.id][direction] = "?"
        next_move = new_move(visited, current_room)

        # print('this is the next move', next_move)
        # When you reach a dead-end (i.e. a room with no unexplored paths),
        # walk back to the nearest room that does contain an unexplored path.
        # if next move is equal to None then initiate new_room
        if next_move == None:
            initial = new_room(traversal_path, visited,
                               current_room, s, reverse)
            print('new_room', initial)
        else:
            traversal_path.append(next_move)
            next_room = current_room.get_room_in_direction(next_move)

            # pop off the room and continue to next room

            # if it has a next move direction then append to traversal_path

            # set the next_room from the current_room

            # print('this is the next room', next_room)
            # if next room is not in visited then set the next room to empty
            if next_room.id not in visited:
                visited[next_room.id] = {}

            # push the reverse direction in the stack
            s.push(reverse[next_move])

            # next loop initial will be the next room id
            initial = next_room.id


traverse(world, traversal_path)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# ######
# UNCOMMENT TO WALK AROUND
# ######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
