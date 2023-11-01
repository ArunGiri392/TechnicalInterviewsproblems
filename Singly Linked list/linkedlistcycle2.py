# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 
# Idea is:
#     1) create two pointer slow and fast, slow moves one step and fast move 2 steps at a Time
#     2) if they meet, it means there is a cycle. Point where they meet may or may not be the start of the cycle. But it is within that cycle.
#     3) to find the starting of cycle, move one pointer to start and keep another pointer where they met, previously, and move them one step at a time until they meet again. The point where they meet this time is the start of the cycle.


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer != None and fast_pointer.next != None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if fast_pointer == slow_pointer:
                # this suggests there is a cycle.
                break
        if fast_pointer == None or fast_pointer.next == None:
            return None
        
        slow_pointer = head
        while slow_pointer != fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        return slow_pointer
