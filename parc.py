class Graph:
    # the list will be a dictionary
    # key will be the vert in question.
    # value will be thelist or set that connects to them
    def __init__(self):
        self.vertices = {}

    # adding the node to compare to '1: {...}'
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    # we are adding and edge btw v1 and v2 '1: {2}'
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


    def bft(self, starting_vertex_id):
        # create an empty que   
        q = Queuse()


        # add starting vertex
        visited = set()

        # create a set for visited

        # while que is not empty
        while q.size( > 0):
            #dequeue a vert
            v = q.dequeue()
        
            # if not visited
            if v not in visited

            # mark as visited
            print(v)
            # add all neighbors to the que
            visited.add(v)

            for neighbor in 

g = Graph()

g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(4, 3)
g.add_edge(3, 6)
g.add_edge(6, 5)
g.add_edge(5, 4)

print(g.vertices)