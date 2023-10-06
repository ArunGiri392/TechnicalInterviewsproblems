
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # The numbers is already given in the reverse form , so this makes our work easier.
        # adding from back can be difficult, it is not possible to traverse from back in linkedlist,so add from front as we traverse.
        # some things to consider are:
        # when adding two numbers, you can get double digit(10) for example. so in that case, we keep the second part(0) and send 1 to the next part.
        # this means we calcualte the quotient and remainder when dividing by 10 and . so we add firstnode.val + secondnode.val + carrry over . 
        # incase of adding 1 2 3 4 + 5, one is less, so what we do?
        # we wait until we reach none of both linked list, to make sure we add everyything and if any linked list becomes None, we keep its value 0.
  #    

#   mistakes i made:
#   1) i increased the temp even when temp reached None, so we do not increase temp, when temp reaches None. 

  # i did not consider cases when 
        temp1 = l1
        temp2 = l2
        # creating a dummy node
        dummy_node = ListNode(0)
        temp = dummy_node
        quotient = 0
        while temp1 != None or temp2 != None:
            if temp1 == None:
                sum =  0 + (temp2.val) + quotient
            elif temp2 == None:
                sum = (temp1.val) + 0  + quotient
            else:
                sum = (temp1.val) + (temp2.val) + quotient
            remainder, quotient = get_remainder_and_quotient(sum)
            temp.next = ListNode(remainder)

            if temp1 != None:
                temp1 = temp1.next
            if temp2 != None:
                temp2 = temp2.next

            temp = temp.next
        
        if quotient != 0:
            temp.next = ListNode(quotient)
            temp = temp.next
        temp.next = None
        
        return dummy_node.next

            
        
        

def get_remainder_and_quotient(number):
    if number < 0:
        raise ValueError("Input number must be non-negative")

    remainder = number % 10
    quotient = number // 10
    return (remainder, quotient)