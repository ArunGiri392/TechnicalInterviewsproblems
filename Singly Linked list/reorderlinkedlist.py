def reorderList(self, head):
      
        # The idea here is to put all the nodes in the list because in linked list, we cannot travel back from last node to second last node.
        # but in list, with help of index, we can acess those nodes.
        # after that, use two pointer concept. and make thenext of first node with last , and increment first and make last node next to second and so.
        # do it while left < right. 
        # here in the list,  we wont have None, so at end we have to add end of some node, so we also keep track of that node while we do this.


        # put all the nodes in the list.
        nodes_array = []
        temp = head
        while temp != None:
            nodes_array.append(temp)
            temp = temp.next
        
        left = 0
        right = len(nodes_array) - 1
        # here we want to keep tracker which would keep track of last node while merging
     # and at last,  we want to make it as a None.
        tracker = nodes_array[left]
        while left < right:
            nodes_array[left].next = nodes_array[right]
            left += 1

            tracker = nodes_array[left]

            # there will be one condition where left will increase and will move to right position. meaning they will at same position.
            # then we do not want to again right to something else, it suggest left and right have merged.

            if nodes_array[left] == nodes_array[right]:
                break

            nodes_array[right].next = nodes_array[left]
            right -= 1

        tracker.next = None
        return head

# Timecomplexity - o(N) because we are traversing the list
# space complexity - o(N) wehre N is the node nodes in the list.

# another way of solving problem:
class Solution(object):
    def reorderList(self, head):
        # idea here is to divide the list into two halves, and reverse the second halves.
        # lets say we have list:
        # 1---2--3---4---5--None

        # then we divide it ,

        # first list becomes -- > 1--2---3--None
        # second list becomes --> 4---5--None

        # reverse the second list: it becomes.
        # 5--->4---> None

        # so list now are: 
        # first list becomes -- > 1--2---3--None
        # second list becomes 5--->4---> None

        # finally, we make connection in this way: 1---5--2---4---3---None
        
        # to divide list, we can use two pointers, one fast and slow, 
        # ie when fast reaches None or fast.next becomes None, slow will have reached in the middle. 

        slow =  head
        fast = head.next
        # when this division happen of the list, the second list will be equal or smaller than the first list. The length of the second list will never be greater than the first list.
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        second_list = slow.next
        slow.next = None
        first = head
        #

        # # reverse the second list.
        prev = None
        current = second_list
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        second = prev
        

        while first != None and second != None:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        #since second list is equal or always smaller than the first list,
        # we dont have to worry about the case what if they is any remaining elements in the second list. cause it is smaller than the first list, we will process each nodes in the second list before we reach None in the first list or in  the second list itself.
        return first

# Timecomplexity - o(N) because we are traversing the list
# space complexity - o(1) No auxillary data structure is being used here.