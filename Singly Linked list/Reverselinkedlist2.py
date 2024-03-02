# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # increaseleft and right pointer, until left pointer does not reach, left.
          # during this, add all nodes, in the dummy node.(part of answer)

        # when i reach left pointer, move the right pointer to the right.
        # when i reach right , save the right.next
        # break the pointer.
        # send, left node to reverselist func,

        # after this add, add reverse nodes, and add, save the right.next

        left_pointer = 1
        right_pointer = 1

        current = head
        dummy_node = ListNode(0)
        temp = dummy_node
        # traversing until left_pointer becomes left, updating dummy node next.
        while left_pointer != left:
            temp.next = current
            temp = temp.next
            current = current.next
            left_pointer += 1
            right_pointer += 1
        
        # saving left_most
        left_most = current
        # incrementing while right_pointer does not equal right value.
        while right_pointer != right:
            current = current.next
            right_pointer += 1
        



        # saving right_pointer.next for later joining.
        next_data = current.next
        # breaking the list.
        current.next = None


        reversed_list = self.reverse_list(left_most)
        current_head = reversed_list
        while current_head != None:
            temp.next = current_head
            temp = temp.next
            current_head = current_head.next
        
        temp.next = next_data
        return dummy_node.next
    
    def reverse_list(self,head):
        current = head
        prev = None
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    


        

        


