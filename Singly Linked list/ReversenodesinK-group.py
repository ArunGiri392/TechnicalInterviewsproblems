# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # The high level idea is send divide each linked list by K and send them to the reverse function. 
        # reverse func reverse the linkedlist we send and we make the dummy node, we traverse through the head of the reverse list and update those nodes in our dummy node.
        # how to send k no of linked list each time to reverse func?
        # make two pointers - slow remains in the head, and fast travels to next until it reaches k nodes. 
        # then we have k nodes, so we make fast.next as None to make that linkedlist seperate and  send it to the reverse function.
        # while we make fast.next = None, we also change the whole original list, so for next iteration, we  save the fast.next, which is the starting point for the next iteration.

        # some mistakes i made here:
        # 1) i  saved fast, but i should have saved fast.next(fast is the part of previous linkedlist) and fast.next shows the new linkedlist.
        # 2) the other is: we continously, move forward fast until count beocmes k , so within the while loop, fast can become None, so 
        # # whenever fast becomes None, we set . temp(dummy node) . next = slow.

        slow = head
        fast = head
        dummy_node = ListNode(0)
        temp = dummy_node

        while fast != None:

            counter = 1
            while fast is not None and  counter < k:
                fast = fast.next
                counter += 1
                # There could be case that while we increment fast, fast can reach to None.
                #so we have to handle it right here, else we get the None object error.
            if fast is None:
                temp.next = slow
                break

            # here we save the fast.next (which would serve as the starting of next linkedlist.)
            temp2 = fast.next
            fast.next = None # here we make none because for the current linkedlist which we want to send to reverse function, we want None.
            reverse_head = reverseList(slow)
            # now we traverse through the linkedlist.
            temp1 = reverse_head

            # update temp (dummy node) with the reverse linked nodes.
            while temp1 != None:
                temp.next = temp1
                temp = temp.next
                temp1 = temp1.next
            
            # then for next iteration , update slow and fast pointer, which is saved by temp2 variable.
            slow = temp2
            fast = temp2

       
        return dummy_node.next


            
# functin to reverse the linked list.
def reverseList(head):
        prev = None
        cur = head

        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head = prev
        return head