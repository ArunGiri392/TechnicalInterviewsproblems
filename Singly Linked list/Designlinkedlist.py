class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        cur = self.head

        while cur != None:
            if index == count:
                return (cur.val)
            cur = cur.next
            count += 1
        return -1

           





        # 1--2--3---None
        # 0  1   2  
        #     #    c


    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            return 
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head= new_node
            return


    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            return 
        
        cur = self.head
        while cur.next != None:
            cur = cur.next
        new_node = Node(val)
        cur.next = new_node
        return


       
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            if self.head == None:
                self.head = Node(val)
                return
            
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            return
        else:
            count = 0
            cur = self.head
            prev = None
            while cur != None:
                if index == count:
                    new_node = Node(val)
                    prev.next = new_node
                    new_node.next = cur
                    return


                prev = cur
                cur = cur.next
                count += 1
            
            if prev == None:
                return
                
            new_node = Node(val)
            prev.next = new_node
            new_node.next = cur
            return
           


              
            #   1--2---3  3,5
            #             c
            #           p
                # count = 3
            #   1 --5--2---3

        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        cur = self.head
        prev = None
        while cur != None:
            if index == count:
                
                prev.next = cur.next
                return


            prev = cur
            cur = cur.next
            count += 1
        
        

        # 1 --2 --3   (2  )
        #     p   c       
        # c= 2


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)