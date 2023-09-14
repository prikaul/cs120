#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root

# init is used to pass initial parameters to the class 
# run python3 *insert name of file* 
# self is not actually an argument, just something used to refer to itself, doesn't really do anything 
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    if v is None: 
        return 0
    else:  
        v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
    return v.size

#
# Problem 1c
#

root = BTvertex(120) 
tree = BinaryTree(root)
tree.root.left = BTvertex(121)
tree.root.right = BTvertex(124)

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 
    # Your code goes here
    # takes in a root vertex v, trying to find the vertex that 
    # program is supposed to return a vertex, that when you remove it, creates the largest subtree that is leq n-2 

    if r is None: 
        return None 
    if r.left is not None and r.left.size > (r.size / 2):
        return find_vertex(r.left)
    elif r.right is not None and r.right.size > (r.size / 2): 
        return find_vertex(r.right)
    else: 
        return r
    
