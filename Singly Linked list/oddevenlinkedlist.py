# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if not head:
            return None
        
        if head.next == None:
            return head
        first_even = head.next
        current = head

        # length
        count = 0
        while current != None:
            count += 1
            current = current.next
        
        current = head
    

        while current != None:
            next_node = current.next
            if current.next and current.next.next:
                current.next = current.next.next
                current = next_node
            else:
                break

        if count % 2 == 0:
            current.next = first_even
        else:
            current.next = None
            next_node.next = first_even
        
        return head
        # Time complexity - O(n)
        # space complexity - o(1)
        


        # if not head:
        #     return None
        
        # if head.next == None:
        #     return head
        
        # dummy_node = ListNode(0)
        # temp = dummy_node
       
        # current = head
        # while current != None:
        #     new_node = ListNode(current.val)
        #     temp.next  = new_node
        #     temp = temp.next
        #     if current.next:
        #         current = current.next.next
        #     else:
        #         break
       
        # # # now for the even case:

        # current = head.next
        # while current != None:
        #     new_node = ListNode(current.val)
        #     temp.next  = new_node
        #     temp = temp.next
        #     if current.next:
        #         current = current.next.next
        #     else:
        #         break

        # temp.next = None
        # return dummy_node.next

        # Time complexity - O(n)
        # space complexity - o(n)
        
        
        
        
        


        # 1 -- 2--3--4--5
        # 1--3--5--2--4