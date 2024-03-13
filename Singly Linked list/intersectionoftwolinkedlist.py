# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # nodes = set()

        # current = headA
        # while current != None:
        #     nodes.add(current)
        #     current = current.next

        # current = headB
        # while current != None:
        #     if current in nodes:
        #         return current
        #     current = current.next
        
        # return None
        # find the difference of two linked list,
        # and whoever is greater in lenght, shift the pointer for that greater linkedlist bydifference, so it gets in advance above,
        # and now again, move them, together, whenever, they p0ooint to same node, thats the interesection.

# Traverse Both Lists and Find Their Lengths: Start by traversing both lists simultaneously and count the number of nodes in each list. This will give you the lengths of both lists.

# Find the Difference in Lengths: Calculate the absolute difference in lengths between the two lists.

# Adjust Starting Points of Pointers: Determine which list is longer and adjust the starting points of the pointers accordingly so that they both start from the same relative position to the end of the longer list.

# Traverse Both Lists Again: Traverse both lists simultaneously with the adjusted pointers until you find the intersection point, or until you reach the end of both lists.

# Return the Intersection Node: If an intersection is found, return the intersecting node. Otherwise, return null.

        current = headA
        lengthofA = 0
        while current != None:
            lengthofA += 1
            current = current.next
        
        current = headB
        lengthofB = 0
        while current != None:
            lengthofB += 1
            current = current.next
        

        A = headA
        B = headB
        if lengthofA > lengthofB:
            difference = lengthofA - lengthofB
            count = 0
            while count != difference:
                A = A.next
                count += 1
        else:
            difference = lengthofB - lengthofA
            count = 0
            while count != difference:
                B = B.next
                count += 1

        while A != None and B != None:
            if A == B:
                return A
            A = A.next
            B = B.next

        return None






     

