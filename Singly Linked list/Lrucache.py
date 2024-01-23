# For this problem, we can use Hashmap and Doubly linked list. 
# Here are all the cases that needs to be considered for the problem 

# There are two dummy pointers : 
# left -- that shows the cache that was not used most recent.
# right -- that shows the cache was used most recent.
# so going left to righ t-- we go not most recent --to -- -most recent. 

# There are two methods: 
# 1) Insert at end -- this method adds a node to the end of the linkedlist(before the right dummy pointer) -- ie it becomes the most recent used cache.
# 2) Delete -- it deltes the node from the linkedlist.

# in  dictionary, we wil keep key as key and value will be the pointer that will point to the address of the node.
# so with the value of any key, we can directly get that particular node.

class Node:
    def __init__(self, key, val):
        # A node wil have key , val and next and prev
        self.key = key
        self.val = val
        self.next = None
        self.Prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # initilaizing two dummy pointers left and right.
        self.left = Node(0, 0)
        self.right = Node(0,0)

        # setting the connection between left and right pointer initially.
        self.left.next = self.right
        self.right.prev = self.left
    
    # insert  node at right(at last)
    def insert(self, node):
        # here we want to insert at last , just before right pointer, so we take reference to right pointer l
        prev = self.right.prev
        next = self.right

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    
    def delete(self, node):
        # when we know, node to be deleted, we changing hte node of previous pointer, and node of next pointer to that node.
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev    

    def get(self, key: int) -> int:
        # possible cases during get.
        # 1) if key is not present , we just return -1. we can check in hashmap if key is present in dictionary or not.
        # 2) if key is present, then the node with this key becomes the most recent one. ie we delete the node with this key from linkedlist wherever it is located and then add it to the end, to make it most recently used. 

        # # the node can be got from the dictionary because we have kept key as key and value as node address.
        if key not in self.cache:
            return -1
        self.delete(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        # There are two cases for put.
        # 1) if key is already present in linkedlist/hashmap --in this case, we just update the value.
        #     ie delete this node from linkedlist and 
        #     insert new node with updated value.
        # 2)    if key is not present,
        #      1) if capcacity is bigger(meaning there is space in cache) than linked list, we just add a new node.
        #      2) if capacity is is smaller(meaning there is not space in cache), then we remove the least recent used cache and add this new node.
        #      so in this case, wehre key is not present, we do add a new node. 
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # next of left give sus which node needs to be deleted.
            node_to_be_removed = self.left.next
            self.delete(node_to_be_removed)
            del self.cache[node_to_be_removed.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)