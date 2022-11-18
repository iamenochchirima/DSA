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


print(tree_to_tuple(tree2))
