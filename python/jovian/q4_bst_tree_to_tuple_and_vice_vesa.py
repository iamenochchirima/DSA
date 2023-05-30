class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

tree_turple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_turple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_turple(data[0])
        node.right = parse_turple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree = parse_turple(tree_turple)

print(tree)

def tree_to_tuple(node):
    if isinstance(node, TreeNode):
        if node.left is None and node.right is None:
            return node.key
        return (
            tree_to_tuple(node.left),
            node.key,
            tree_to_tuple(node.right)
        )
    return node



# from q3_data_structure_for_a_social_network import User, UserDatabase

# """
# QUESTION: Implement a binary tree using Python, and show its usage with some examples.


# class TreeNode:
#     def __init__(self, key):
#         self.key  = key
#         self.left = None
#         self.right = None

# node0 = TreeNode(3)
# node1 = TreeNode(4)
# node2 = TreeNode(5)

# node0.left = node1
# node0.right = node2

# tree = node0
# """

# class TreeNode:

#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

# tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

# def parse_tuple(data):
    
#     if isinstance(data, tuple) and len(data) == 3:
#         node = TreeNode(data[1])
#         node.left = parse_tuple(data[0])
#         node.right = parse_tuple(data[2])
#     elif data is None:
#         node = None
#     else:
#         node = TreeNode(data)
#     return node

# tree2 = parse_tuple(tree_tuple)


# """
# QUESTION: Define a function tree_to_tuple that converts a binary tree into a tuple representing the 
# same tree. E.g. tree_to_tuple converts the tree created above to the tuple ((1, 3, None), 2, ((None, 
# 3, 4), 5, (6, 7, 8))). Hint: Use recursion.
# """

# def tree_to_tuple(node):
#     if isinstance(node, TreeNode):
#         if node.left is None and node.right is None:
#             return node.key
#         return (
#             tree_to_tuple(node.left),
#             node.key,
#             tree_to_tuple(node.right)
#         )
#     else:
#         return node

# """
# A function to display the tree structure
# """

# def display_keys(node, space='\t', level=0):
#     # print(node.key if node else None, level)
    
#     # If the node is empty
#     if node is None:
#         print(space*level + '∅')
#         return   
    
#     # If the node is a leaf 
#     if node.left is None and node.right is None:
#         print(space*level + str(node.key))
#         return
    
#     # If the node has children
#     display_keys(node.right, space, level+1)
#     print(space*level + str(node.key))
#     display_keys(node.left,space, level+1) 

# def travers_in_order(node):
#     if node is None:
#         return []
#     return (
#         travers_in_order(node.left) + 
#         [node.key] +
#         travers_in_order(node.right)
#     )   

# def travers_pre_order(node):
#     if node is None:
#         return []
#     return (
#         [node.key] +
#         travers_pre_order(node.left) + 
#         travers_pre_order(node.right)
#     )  

# def travers_post_order(node):
#     if node is None:
#         return []
#     return (
#         travers_post_order(node.left) + 
#         travers_post_order(node.right) +
#         [node.key]
#     )  

# """
# QUESTION: Write a function to calculate the height/depth of a binary tree
# """

# def tree_height(node):
#     if node is None:
#         return 0
#     return 1 + max(tree_height(node.left), tree_height(node.right))

# print(tree_height(tree2))

# """
# QUESTION: Write a function to count the number of nodes in a binary tree
# """

# def treeSize(node):

#     if node is None:
#         return 0
#     return 1 + treeSize(node.left) + treeSize(node.right)

# """ 
# Encapsulation everything
# """

# class TreeNode():
#     def __init__(self, key):
#         self.key, self.left, self.right = key, None, None
    
#     def height(self):
#         if self is None:
#             return 0
#         return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
#     def size(self):
#         if self is None:
#             return 0
#         return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

#     def traverse_in_order(self):
#         if self is None: 
#             return []
#         return (TreeNode.traverse_in_order(self.left) + 
#                 [self.key] + 
#                 TreeNode.traverse_in_order(self.right))
    
#     def display_keys(self, space='\t', level=0):
#         # If the node is empty
#         if self is None:
#             print(space*level + '∅')
#             return   

#         # If the node is a leaf 
#         if self.left is None and self.right is None:
#             print(space*level + str(self.key))
#             return

#         # If the node has children
#         display_keys(self.right, space, level+1)
#         print(space*level + str(self.key))
#         display_keys(self.left,space, level+1)    
    
#     def to_tuple(self):
#         if self is None:
#             return None
#         if self.left is None and self.right is None:
#             return self.key
#         return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
#     def __str__(self):
#         return "BinaryTree <{}>".format(self.to_tuple())
    
#     def __repr__(self):
#         return "BinaryTree <{}>".format(self.to_tuple())
    
#     @staticmethod    
#     def parse_tuple(data):
#         if data is None:
#             node = None
#         elif isinstance(data, tuple) and len(data) == 3:
#             node = TreeNode(data[1])
#             node.left = TreeNode.parse_tuple(data[0])
#             node.right = TreeNode.parse_tuple(data[2])
#         else:
#             node = TreeNode(data)
#         return node

# """
#  QUESTION: Write a function to check if a binary tree is a binary search tree (BST).

# QUESTION: Write a function to find the maximum key in a binary tree.

# QUESTION: Write a function to find the minimum key in a binary tree.
# """

# def remove_none(nums):
#     return [x for x in nums if x is not None]

# def is_bst(node):
#     if node is None:
#         return True, None, None
    
#     is_bst_l, min_l, max_l = is_bst(node.left)
#     is_bst_r, min_r, max_r = is_bst(node.right)
    
#     is_bst_node = (is_bst_l and is_bst_r and 
#               (max_l is None or node.key > max_l) and 
#               (min_r is None or node.key < min_r))
    
#     min_key = min(remove_none([min_l, node.key, min_r]))
#     max_key = max(remove_none([max_l, node.key, max_r]))
    
#     # print(node.key, min_key, max_key, is_bst_node)
        
#     return is_bst_node, min_key, max_key

# """
# Storing Key-Value Pairs using BSTs 
# """

# class BSTNode():
#     def __init__(self, key, value=None):
#         self.key = key
#         self.value = value
#         self.left = None
#         self.right = None
#         self.parent = None

# # Level 0

# names = aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
# biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
# hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
# enoch = User('enoch', 'Enoch Chirima', 'enoch@gmail.com')
# siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
# sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
# vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

# #Level 0
# tree = BSTNode(enoch.username, enoch) 

# # Level 1
# tree.left = BSTNode(biraj.username, biraj)
# tree.left.parent = tree
# tree.right = BSTNode(sonaksh.username, sonaksh)
# tree.right.parent = tree

# def insert(node, key, value):
#     if node is None:
#         node = BSTNode(key, value)
#     elif key < node.key:
#         node.left = insert(node.left, key, value)
#         node.left.parent = node
#     elif key > node.key:
#         node.right = insert(node.right, key, value)
#         node.right.parent = node
#     return node

# insert(tree, biraj.username, biraj)
# insert(tree, sonaksh.username, sonaksh)
# insert(tree, aakash.username, aakash)
# insert(tree, hemanth.username, hemanth)
# insert(tree, siddhant.username, siddhant)
# insert(tree, vishal.username, siddhant)

# """  
# Finding a Node in BST
# QUESTION: Find the value associated with a given key in a BST.
# """

# def find(node, key):
#     if node is None:
#         return None
#     if key == node.key:
#         return node
#     if key < node.key:
#         return find(node.left, key)
#     if key > node.key:
#         return find(node.right, key)



# node = find(tree, 'enoch')

# """ 
# Updating a value in a BST
# QUESTION: Write a function to update the value associated with a given key within a BST
# """

# def update(node, key, value):
#     target = find(node, key)
#     if target is not None:
#         target.value = value

# update(tree, 'enoch', User('enock', 'Enock Ngoni', 'enochn@example.com'))

# node = find(tree, 'enock')

# """
# List the nodes
# QUESTION 13: Write a function to retrieve all the key-values pairs stored in a BST in the sorted 
# order of keys.  
# """

# def list_all(node):
#     if node is None:
#         return []
#     return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

# """
# Balanced Binary Trees
# QUESTION: Write a function to determine if a binary tree is balanced.  
# """

# def is_balanced(node):
#     if node is None:
#         return True, 0
#     balanced_l, height_l = is_balanced(node.left)
#     balanced_r, height_r = is_balanced(node.right)
#     balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
#     height = 1 + max(height_l, height_r)
#     return balanced, height

# """
# Balanced Binary Search Trees
# QUESTION: Write a function to create a balanced BST from a sorted list/array of key-value pairs.  
# """

# def make_balanced_bst(data, lo=0, hi=None, parent=None):
#     if hi is None:
#         hi = len(data) - 1
#     if lo > hi:
#         return None
    
#     mid = (lo + hi) // 2
#     key, value = data[mid]

#     root = BSTNode(key, value)
#     root.parent = parent
#     root.left = make_balanced_bst(data, lo, mid-1, root)
#     root.right = make_balanced_bst(data, mid+1, hi, root)
    
#     return root
    
# """
# Balancing an Unbalanced BST
# QUESTION: Write a function to balance an unbalanced binary search tree.  
# """

# def balance_bst(node):
#     return make_balanced_bst(list_all(node))

# tree1 = None

# for user in users:
#     tree1 = insert(tree1, user.username, user)

# """
# A Python-Friendly Treemap
# We are now ready to return to our original problem statement.

# QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:

# Insert the profile information for a new user.
# Find the profile information of a user, given their username
# Update the profile information of a user, given their usrname
# List all the users of the platform, sorted by username
# You can assume that usernames are unique.
# """

# class TreeMap():
#     def __init__(self):
#         self.root = None
        
#     def __setitem__(self, key, value):
#         node = find(self.root, key)
#         if not node:
#             self.root = insert(self.root, key, value)
#             self.root = balance_bst(self.root)
#         else:
#             update(self.root, key, value)
            
        
#     def __getitem__(self, key):
#         node = find(self.root, key)
#         return node.value if node else None
    
#     def __iter__(self):
#         return (x for x in list_all(self.root))
    
#     def __len__(self):
#         return tree_size(self.root)
    
#     def display(self):
#         return display_keys(self.root)




