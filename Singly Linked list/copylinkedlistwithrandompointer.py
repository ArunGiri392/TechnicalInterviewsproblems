
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # The logic is:
        # 1) Traverse through original linkedlist, then, create a copy node of that linkedlist, based on orignal value, keep Next and random, as None , because we do not know, 
        # as we create a  copy node, then we store the original node as key and copy node as value in hashmap.
        # then, again traverse through linkedlist, and based on original linked list, we can access the copy of that node, through hasmap, then for that copy node, we just need to set next and random pointer . how do we do this?
        # becauase, we have  acess to original node, we can get acess to  origianl next and random node, and copy of these are present in hashmap, because we have added all copy nodes in hashmap previosuly. so just access them with the help of orignal node, and set them.
        if not head:
            return None
        original_copy = {}
        # original:copy
        current_node = head
        while current_node != None:
            copy_node = Node(current_node.val, None, None)
            original_copy[current_node] = copy_node
            current_node = current_node.next
     
        
        # 1--- 2--N
        #         c
        # traverse through linkedlist to set next and random pointer of  copy nodes.
        current = head
        while current != None:
            copy_node = original_copy[current]
            # if we do not do this then, any node can have its current, or random as None, prrety much possible, 
            # then, if we do not have if condition then, original_copy[current.next] will be calculated, and current.next is None, then orignal_copy[None] becomes, but None is never our key, so it rasies key error.
            if current.next:
                 copy_node.next = original_copy[current.next]
            if current.random:
                 copy_node.random = original_copy[current.random]
            current = current.next
        
        # we could also achieve same thing by iterating through hashmap.
        # for node in original_copy:
        #     original_next = node.next
        #     original_random = node.random
            
        #     if original_next:
        #          original_copy[node].next = original_copy[original_next]
        #     if original_random:
        #          original_copy[node].random = original_copy[original_random]
        
        # set head of copy list.
        copy_head = original_copy[head]
        return copy_head


