from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Translate into graphs languege:
    # nodes: rooms
    # edges: n,s,e,w

# Build graph, or define getNeighbors()

# Choose your algorithm. (BFS)



# write algorithm to traverse through the map:
# `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)`

# picks a random unexplored direction from the player's current room

# travels and logs that direction

# then loops

# if we run into a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path

def victory():
    # Load world
    world = World()
    q = Queue()
    visited = set()
    movements = []
    # get the possible exits for the room
    # chooses n,s,e,w randomly based on the exits avaliable.
    for exits in player.current_room.get_exits():
        direction = player.travel(random.choice(exits))
        movements.append(direction)

    traversal_path.append(movements)


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# ######
# UNCOMMENT TO WALK AROUND
# ######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
