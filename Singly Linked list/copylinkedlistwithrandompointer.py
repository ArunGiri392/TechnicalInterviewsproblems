"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
         # The logic is:
        # 1) Traverse through original linkedlist, then, create a copy node of that linkedlist, based on orignal value, keep Next and random, as None , because we do not know, 
        # as we create a  copy node, then we store the original node as key and copy node as value in hashmap.
        # then, again traverse through linkedlist, and based on original linked list, we can access the copy of that node, through hasmap, then for that copy node, we just need to set next and random pointer . how do we do this?
        # becauase, we have  acess to original node, we can get acess to  origianl next and random node, and copy of these are present in hashmap, because we have added all copy nodes in hashmap previosuly. so just access them with the help of orignal node, and set them.
        if not head:
            return None
        container = {}

        current = head
        # setting original node as key and new node as value.
        while current:
            new_node = Node(current.val)
            container[current] =  new_node
            current = current.next
        
        for node in container:
            new_node = container[node]
            # why to check if node.next or node.random?
            # if we do not do this then, any node can have its current, or random as None, prrety much possible, 
            # then, if we do not have if condition then, original_copy[current.next] will be calculated, and if current.next is None, then orignal_copy[None] becomes, but None is never our key, so it rasies key error.

            if node.next:
                #new_node.next = node wont work becuase on doing so we set the next pointer of our new nod to the original node which is not allowed
                new_node.next = container[node.next]
            if node.random:
                new_node.random = container[node.random]

           
                
        return container[head]