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
    pass


# section exercises 
# given a string s, write a recursive algorithm to determine if palindrome or not
# RECURSIVE

def palindrome(s): 
    newstring = ""
    for i in range(len(s)): 
        newstring = newstring + s[len(s) - i + 1]
    if newstring == s: 
        print("palindrome") 
    else: 
        print("not a palindrome")

def is_palindrome(s): 
    if (len(s)) <= 1: 
        return True
    if (s[0] != s[len(s) - 1]): 
        return False
    new_s = s[1: len(s) - 1]
    return is_palindrome(new_s)

class Tree: 
    children: []
    key: int
    temp: int

def populateTemp(T): 
    for i in range(len(T.children)): 
        T.children[i].temp = len(T.children[i])

def populateTemp(T): 
    T.temp = len(T.children)
    for subtree in T.children: 
        populateTemp(subtree)

# the above doesn't return anything, just sets the temp field in each thingy. 

def elementExists(T, target): 
    if T.temp is target: 
        return True
    for subtree in T.children: 
        if elementExists(subtree, target): 
            return True
    return False