# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return head

        # set current1 and prev1   
        current1 = head
        counter = 1
        prev1 = None
        while current1 != None and counter != k:
            prev1 = current1
            current1 = current1.next
            counter += 1
        
        length = 0
        current = head
        while current != None:
            current = current.next
            length += 1
        
        actual_length = length - k

        # set current2 and prev2  
        current2 = head
        counter = 0
        prev2 = None
        while current2 != None and counter != actual_length:
            prev2 = current2
            current2 = current2.next
            counter += 1
        
        # if we are trying to swap same node, then there is no need to swap.
        if current1 == current2:
            return head


        # start swapping.
        # if prev1 exists, change prev1 pointer.
        if prev1:
            prev1.next = current2
        # if not, set the new head as current2.
        else:
            head = current2
        
        if prev2:
            prev2.next = current1
        else:
            head = current1
        
        # swap, current1.next, current2.next to eachother.
        temp = current2.next   
        current2.next = current1.next
        current1.next = temp
        return head



       

        

