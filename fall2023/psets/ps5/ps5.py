from itertools import product, combinations
import random

'''
Before you start: Read the README and the Graph implementation below.
'''

class Graph:
    '''
    A graph data structure with number of nodes N, list of sets of edges, and a list of color labels.

    Nodes and colors are both 0-indexed.
    For a given node u, its edges are located at self.edges[u] and its color is self.color[u].
    '''

    # Initializes the number of nodes, sets of edges for each node, and colors
    def __init__(self, N, edges = None, colors = None):
        self.N = N
        self.edges = [set(lst) for lst in edges] if edges is not None else [set() for _ in range(N)]
        self.colors = [c for c in colors] if colors is not None else [None for _ in range(N)]
    
    # Adds a node to the end of the list
    # Returns resulting graph
    def add_node(self):
        self.N += 1
        self.edges.append(set())
        return self
    
    # Adds an undirected edge from u to v
    # Returns resulting graph
    def add_edge(self, u, v):
        assert(v not in self.edges[u])
        assert(u not in self.edges[v])
        self.edges[u].add(v)
        self.edges[v].add(u)
        return self

    # Removes the undirected edge from u to v
    # Returns resulting graph
    def remove_edge(self, u, v):
        assert(v in self.edges[u])
        assert(u in self.edges[v])
        self.edges[u].remove(v)
        self.edges[v].remove(u)
        return self

    # Resets all colors to None
    # Returns resulting graph
    def reset_colors(self):
        self.colors = [None for _ in range(self.N)]
        return self

    def clone(self):
        return Graph(self.N, self.edges, self.colors)

    def clone_and_merge(self, g2, g1u, g2v):
        '''
        DOES NOT COPY COLORS
        '''
        g1 = self
        edges = g1.edges + [[v + g1.N for v in u_list] for u_list in g2.edges]
        g = Graph(g1.N + g2.N, edges)
        if g1u is not None and g2v is not None:
            g = g.add_edge(g1u, g2v + g1.N)
        return g

    # Checks all colors
    def is_graph_coloring_valid(self):
        for u in range(self.N):
            for v in self.edges[u]:

                # Check if every one has a coloring
                if self.colors[u] is None or self.colors[v] is None:
                    return False

                # Make sure colors on each edge are different
                if self.colors[u] == self.colors[v]:
                    return False
        
        return True

'''
    Introduction: We've implemented exhaustive search for you below.

    You don't need to implement any extra code for this part.
'''

# Given an instance of the Graph class G, exhaustively search for a k-coloring
# Returns the coloring list if one exists, None otherwise.
def exhaustive_search_coloring(G, k=3):

    # Iterate through every possible coloring of nodes
    for coloring in product(range(0,k), repeat=G.N):
        G.colors = list(coloring)
        if G.is_graph_coloring_valid():
            return G.colors

    # If no valid coloring found, reset colors and return None
    G.reset_colors()
    return None


'''
    Part A: Implement two coloring via breadth-first search.

    Hint: You will need to adapt the given BFS pseudocode so that it works on all graphs,
    regardless of whether they are connected.

    When you're finished, check your work by running python3 -m ps5_color_tests 2.
'''

# Given an instance of the Graph class G and a subset of precolored nodes,
# Assigns precolored nodes to have color 2, and attempts to color the rest using colors 0 and 1.
# Precondition: Assumes that the precolored_nodes form an independent set.
# If successful, modifies G.colors and returns the coloring.
# If no coloring is possible, resets all of G's colors to None and returns None.
def bfs_2_coloring(G, precolored_nodes=None):
    # Assign every precolored node to have color 2
    # Initialize visited set to contain precolored nodes if they exist
    visited = set()
    G.reset_colors()
    preset_color = 2
    if precolored_nodes is not None:
        for node in precolored_nodes:
            G.colors[node] = preset_color
            visited.add(node)

        if len(precolored_nodes) == G.N:
            return G.colors
    
    # TODO: Complete this function by implementing two-coloring using the colors 0 and 1.
    # If there is no valid coloring, reset all the colors to None using G.reset_colors()
    # pri starts here
    start = random.choice(range(G.N)) # picks a random vertex out of the N available 
    # next we need BFS to create an order of vertices 
    # need to initialize an empty set 
    bfs_order = [start]
    # now want to enqueue the ones that are neighbors
    # need to keep track of already visited nodes somehow
    visited.add(start)
    # now need to access the neighbors of the start vertex: 
    # next vertices, the set of hte next vertices you can go to in BFS 
    next_vertices = [start]
    # add those to the bfs_order 
    # now need to add these new vertices to the visited set 
    # now need to repeat this process on everything that's NOT in visited
    # this = start
    while next_vertices: #while there are still more vertices to traverse 
        this = next_vertices[0] # accesses one of the next vertices 
        next_vertices.remove(this) # takes it off of the list of next_vertices
        for i in G.edges[this]:
            if i not in visited: 
                bfs_order.append(i)
                visited.add(i)
                next_vertices.append(i)
    
    # Set the color of the start vertex to 0
    G.colors[start] = 0
    bfs_order.remove(start)
    avail_colors = {0, 1} # set of available colors
    for i in bfs_order: 
        for j in G.edges[i]: 
            if G.colors[j] is not None: # they are all the same color
                G.colors[i] = (avail_colors - {G.colors[j]}).pop() # sets it to a diff color 
                # check this 
                if G.colors[j] is None:  
                    G.reset_colors()
                    return None
                # check
    
    # G.reset_colors()
    return G.colors

'''
    Part B: Implement is_independent_set.
'''

# Given an instance of the Graph class G and a subset of precolored nodes,
# Checks if subset is an independent set in G 
def is_independent_set(G, subset):
    # TODO: Complete this function
    # pri starts here 
    for vertex in subset:
        # go through the edges of the vertex, see if any of them are in the subset 
        for i in G.edges[vertex]:
            if i in subset:
                return False 
    return True

'''
    Part C: Implement the 3-coloring algorithm from the sender receiver exercise.
    
    Make sure to call the bfs_2_coloring and is_independent_set functions that you already implemented!

    Hint 1: You will want to use the Python `combinations` function from the itertools library
    to enumerate all possible independent sets. Remember that each element of combinations is a tuple,
    so you may need to convert it to a list.

    Hint 2: Python itertools functions compute their results lazily, which means that they only
    calculate each element as the program requests it. This saves time and space, since it
    doesn't need to store the entire list of combinations up front. You should NOT try to convert the result
    of the entire combinations call to a list, since that will force Python to precompute everything.
    Instead, you should iterate over them in a for loop, which will maintain the lazy behavior we want.
    See the call to "product" in exhaustive_search for an example.

    When you're finished, check your work by running python3 -m ps5_color_tests 3.
    Don't worry if some of your tests time out: that is expected.
'''

# Given an instance of the Graph class G (which has a subset of precolored nodes), searches for a 3 coloring
# If successful, modifies G.colors and returns the coloring.
# If no coloring is possible, resets all of G's colors to None and returns None.
def iset_bfs_3_coloring(G):
    # TODO: Complete this function.
    # pri starts here 
    # find one independent set, and 2 color the other two 
    # sizes from 1 to n/3, iterates through all possible combinations of that size, each time 
    # checking if it's an independent set. if it is then input into 2-colorable, 
    # everything in the independent set is the 3rd color, everything not in the independent set 
    # is 2 colorable, you put that into your bfs2color function 
    # go from 0 to n/3
    # return none at the bottom ? / have a 0 case 
    n = G.N
    for i in range(0, n/3 + 1): # check this 
        for subset in combinations(G.N, i): # combinations takes in 
            if is_independent_set(G, subset): 


    G.reset_colors()
    return None

# Feel free to add miscellaneous tests below!
if __name__ == "__main__":
    G0 = Graph(2).add_edge(0, 1)
    print(bfs_2_coloring(G0))
    print(iset_bfs_3_coloring(G0))
