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
        print(data)
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = parse_tuple(((1,3,None),2,((None,3,4),5,(6,7,8))))
