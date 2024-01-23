class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # This soln basically creates a new pointer s , and keeps on updating the smallest element.
    # we also set head of list as s after first if and else, cause we want to keep track of the head of list.

    def mergeTwoLists(self, p, q):
        s = None
        if p == None:
            return q
        if q == None:
            return p

        if p.val < q.val:
            s = p
            p = p.next
        else:
            s = q
            q = q.next
        # setting up the head
        new_head  = s

        while p != None and q != None:
            if p.val < q.val:
                s.next = p
                s = p
                p = p.next
            else:
                s.next = q
                s = q
                q = q.next
        
        if p == None:
            s.next = q
        if q == None:
            s.next = p
        return new_head
    
    # this process deals with creating a dummy node and using it to solve the problem.
    def merge_list(self,p,q):
        # This soln uses a dummy node which simplifies many operations . as compared to the previous process.
        # using a dummy node.
        dummy =  ListNode(0)
        temp = dummy
        while p != None and q != None:
            if p.val < q.val:
                temp.next = p
                p = p.next
            else:
                temp.next = q
                q = q.next
            temp = temp.next
        if p == None:
            temp.next = q
        if q == None:
            temp.next = p
        return dummy.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        dummy_node = ListNode(0)
        temp3 = dummy_node

        while temp1 != None and temp2 != None:
            if temp1.val < temp2.val:
                temp3.next = temp1
                temp1 = temp1.next
            else:
                temp3.next = temp2
                temp2 = temp2.next
            temp3 = temp3.next
        
        if temp1 == None:
            temp3.next = temp2
        else:
            temp3.next = temp1
        return dummy_node.next


            