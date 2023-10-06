class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self,data,node):
        new_node = Node(data)
        current_node = self.head
        # end loop if next of current node is null or if current node data is equal to node provided by user
        while current_node != None and current_node.data != node:
            current_node = current_node.next
        # if current node is none meaning we traverse all the linkedlist and did not find the node to be addded after.
          #handling the case, if the provided key is not in the list.
        if current_node == None:
            print("There is no data you are looking for")
        else:
            new_node.next = current_node.next
            current_node.next = new_node
        
      
        
    def deleting_by_value(self,node):
        if self.head == None:
            return
        
         #if the deleted node is supposed to be the first node.
        if self.head.data == node:
            self.head = self.head.next
            return
    
        
        current_node = self.head
        previous_node = None
        
        while current_node != None and current_node.data != node:
            previous_node = current_node
            current_node = current_node.next
        #handling the case, if the provided node is not in the list.   
        if current_node == None:
            print("There is not a node to be deleted")
        else:
            previous_node.next = current_node.next
            current_node = None
    
    def swap_nodes(self,key1, key2):
        #if both key are same, then there is no need to swap the nodes.
        if key1 == key2:
            return
        # creating pointers that traverse through linkedlist and track current node and previous node. 
        #This should be done for both the nodes(so in total 4 pointers is needed. 2 for current, and 2 for previous)
        first_current_node = self.head
        first_previous_node = None
        while first_current_node != None and first_current_node.data != key1:
            first_previous_node = first_current_node
            first_current_node = first_current_node.next
       
        second_current_node = self.head
        second_previous_node = None
        while second_current_node != None and second_current_node.data != key2:
            second_previous_node = second_current_node
            second_current_node = second_current_node.next
        
        if first_current_node == None or second_current_node == None:
            print("One of the node to swap is missing. Please provide the right nodes to be swapped.")
        # If previous node for first node is not null, it means it is not a first node. so there is a previous node.
        # if previous node for first node is null, it means there is nothing in front of it, so it is a first node, so we have to handle it seperately.
        if first_previous_node != None:
            first_previous_node.next = second_current_node
        else:
            self.head = second_current_node

        if second_previous_node != None:
            second_previous_node.next = first_current_node
        else:
            self.head = first_current_node

        temp = first_current_node.next
        first_current_node.next = second_current_node.next
        second_current_node.next = temp
    
    def reverse_linked_list(self):
        current_node = self.head
        previous_node = None
        while current_node != None:
           temp = current_node.next
           current_node.next = previous_node
           previous_node = current_node
           current_node = temp
    
        # setting the head of the list.   
        self.head = previous_node
        
    def merge_sorted(self,list):
        p = self.head
        q = list.head

        if p == None :
            return q
        if q == None:
            return p
        
        if p.data <= q.data:
            s = p
            p = p.next
        else:
            s = q
            q = q.next 
        newhead = s

        while p != None and q != None:
            if p.data <= q.data:
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
        return newhead




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    def print_list(self):
        temp = self.head
        linkedlist = ""
        while temp != None:
            linkedlist += str(temp.data) + "--->"
            temp = temp.next
        print(linkedlist + "None")

linkedlist = LinkedList()
linkedlist.append("A")
linkedlist.append("B")
linkedlist.prepend("C")
print("Linkedlist after appending and prepending elements")
linkedlist.print_list()
linkedlist.insert_after_node("F","B")
print("Linkedlist after adding nodes after B node")
linkedlist.print_list()
linkedlist.deleting_by_value("A")
print("Linkedlist after deleting node A")
linkedlist.print_list()
linkedlist.swap_nodes("C","F")
print("Linkedlist after swapping nodes C and F")
linkedlist.print_list()

linkedlist.reverse_linked_list()
print("linkedlist after reversing it")
linkedlist.print_list()

secondlist = LinkedList()
secondlist.append(1)
secondlist.append(2)
secondlist.append(3)
secondlist.append(4)
secondlist.print_list()
secondlist.reverse_linked_list()
print("linkedlist after reversing it")
secondlist.print_list()