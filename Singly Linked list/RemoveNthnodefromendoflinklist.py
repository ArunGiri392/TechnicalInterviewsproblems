def removeNthFromEnd(self, head, n):
       # the first approach is:
    #    firstly calculate the length of linklist and after that , if we subtract the n from length,
    #    we will reacht the node to be delted. so we also track the previous node and delete it.
    #    the edge case, if if there is only a single node, then we have to handle it seperately before going to loop
    #     # 
        if head.next == None:
            head = None
            return head
        # calculate the length of linkedlist
        length = 0
        temp = head
        while temp != None:
            length += 1
            temp = temp.next
        
        # calculating where to stop.
        stop = length - n
        previous = None
        current = head
        count = 0

        # if there is only one node and if we want to delete it, it has to handled before going to loop.
        if count == stop:
            head = head.next
            return head
        # untile we reach the end, 
        while current != None:
            # if count and stop are equal, it means we reach the node to be deletd.
            if count == stop:
                previous.next = current.next
                return head
            count += 1
            previous = current
            current = current.next

        # another approach.
#        This process invovles keeping two pointer and by creating a dummy node.
# create dummy node and point it to head.
# point fist pointer to dummy node and second pointer to head.
# now, we want to keep second pointer n steps away from first pointer.
# and when we keep n step away, and after that, if we move both of them until second pointer reaches none,
# then first pointer will reach to the node to be deleted. this is because, on first iteration,we set up that gap right and 
# later when we move both pointers and second pointer reaches none, first pointer reaches to node to be deleted.
       
       # by creating a dummy node:

        dummy_node = ListNode(0)
        dummy_node.next = head

        first_pointer = dummy_node
        second_pointer  = head

    
        count = 0
    #we want to keep second pointe n steps away from first node at first 
        while count < n:
              second_pointer = second_pointer.next
              count += 1

        # now move second pointer until it reaches none such taht first pointer reaches node to be deleted.
        while second_pointer != None:
           first_pointer = first_pointer.next
           second_pointer = second_pointer.next

    # after this,second pointer is on the null.
    # fist pointer is in the previous node of node to be delted.
        first_pointer.next = first_pointer.next.next
        return dummy_node.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        counter = 0
        while counter != n:
            fast = fast.next
            counter += 1
        
       
    
        previous_node = None
        while fast != None:
            previous_node = slow
            slow = slow.next
            fast = fast.next
        
        if slow == head:
            return head.next
    
        previous_node.next = slow.next
        return head

        