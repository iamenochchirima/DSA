'''
Your objective in this assignment is to implement a HashTable class which supports the following 
operations:

Insert: Insert a new key-value pair
Find: Find the value associated with a key
Update: Update the value associated with a key
List: List all the keys stored in the hash table
'''

class HashTable:
    def insert(self, key, value):
        """Insert a new key-value pair"""
        pass
    
    def find(self, key):
        """Find the value associated with a key"""
        pass
    
    def update(self, key, value):
        """Change the value associated with a key"""
        pass
    
    def list_all(self):
        """List all the keys"""
        pass


MAX_HASH_TABALE_SIZE = 4096

data_list = [None] * 4096



def get_index(data_list, a_string):

    result = 0

    for charector in a_string:
        a_value = ord(charector)
        result += a_value

    list_index = result % len(data_list)

    return list_index


'''
Insert

To insert a key-value pair into a hash table, we can simply get the hash of the key, and store the 
pair at that index in the data list.
'''


