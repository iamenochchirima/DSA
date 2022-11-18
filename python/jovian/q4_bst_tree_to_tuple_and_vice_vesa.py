"""
QUESTION: Implement a binary tree using Python, and show its usage with some examples.


class TreeNode:
    def __init__(self, key):
        self.key  = key
        self.left = None
        self.right = None

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0.left = node1
node0.right = node2

tree = node0
"""

class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):
    
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = parse_tuple(tree_tuple)


"""
QUESTION: Define a function tree_to_tuple that converts a binary tree into a tuple representing the 
same tree. E.g. tree_to_tuple converts the tree created above to the tuple ((1, 3, None), 2, ((None, 
3, 4), 5, (6, 7, 8))). Hint: Use recursion.
"""

def tree_to_tuple(node):
    if isinstance(node, TreeNode):
        if node.left is None and node.right is None:
            return node.key
        return (
            tree_to_tuple(node.left),
            node.key,
            tree_to_tuple(node.right)
        )
    else:
        return node

"""
A function to display the tree structure
"""

def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1) 

def travers_in_order(node):
    if node is None:
        return []
    return (
        travers_in_order(node.left) + 
        [node.key] +
        travers_in_order(node.right)
    )   

def travers_pre_order(node):
    if node is None:
        return []
    return (
        [node.key] +
        travers_pre_order(node.left) + 
        travers_pre_order(node.right)
    )  

def travers_post_order(node):
    if node is None:
        return []
    return (
        travers_post_order(node.left) + 
        travers_post_order(node.right) +
        [node.key]
    )  

"""
QUESTION: Write a function to calculate the height/depth of a binary tree
"""

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

print(tree_height(tree2))

"""
QUESTION: Write a function to calculate the height/depth of a binary tree
"""

def treeSize(node):

    if node is None:
        return 0
    return 1 + treeSize(node.left) + treeSize(node.right)

""" 
Encapsulation everything
"""