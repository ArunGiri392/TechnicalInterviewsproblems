class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        # if self.key is None, that means, tree is empty currently and we make key as data
        if self.key == None:
            self.key = data
            return
        # This is to not allow duplicate.
        # if root.key is equal to data given, it suggest we are trying to add value that already exist
        # and we just return dont do anything(will not add )
        if self.key == data:
            return 
        # Now, we want to add. so we have to figure out which side to add (left or right)
        # if root.key is greater than data given, meaning data is smaller then we go to left side.
         # if root.key is smaller than data given, meaning data is greater then we go to right side.

        if self.key > data:
            # Here we have to consider two cases before adding any node.
            # if current root left child is none, meaning it does not have left child, just add it
            # if current root left child is not none , meaning it does have a left child then
            # we have to recursively, call insert method by passing the left child
            # self.lchild (by doing this we pass child) and call insert on the child
            # this recurison goes on
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            # same applies for the right side too.
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    
    def search(self, data):
        # firstly, we check if root(ie self).node == data, if yes, we found the the node.
        if self.key == data:
            print("Node is found")
            return
        #If we do not find the node, then , we check if data is smaller or greater than the root value
        # if data is smaller than the root value, then we have to look on the left side.
        # if data is greater than the root value, then we have to look on the right side.
        if data < self.key:
            # here if data is smaller then root value, it means we are looking on left side.
            # Here , we have to consider two cases.
            #1#) if there is no left child of the root , that means, we came to end and node is not present
            #2) if there is left child, then we call search function again , with our self changing to self.child
            #meaning in this case, self would be self.lchild 
            # and this process would happen recursively .

            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node IS NOT PRESENT")
        else:
            # similar idea for the right side too.
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")

    def preorder(self):
        #firstly, we print the root at which we are:
        print(self.key, end = " ")
        # if root has left child, then recursively call preorder on it.
        if self.lchild:
            self.lchild.preorder()
        # if root has right child, then recursively call preoder on it.
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
    

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end = " ")
    
    def level_order(self):
        if self == None:
            return None
        # creating an empty queue.
        queue = []
        queue.append(self)

        while queue:
            # dequeu a node from the front of the queue
            current_node = queue.pop(0)
            print(current_node.key, end = " ")
            if current_node.lchild:
                queue.append(current_node.lchild)
            if current_node.rchild:
                queue.append(current_node.rchild)
    
    def level_order_withNull(self):
        if self is None:
            return None

        # Create an empty queue
        queue = []
        queue.append(self)

        while queue:
            current_node = queue.pop(0)
            if current_node is None:
                print("None", end=" ")
            else:
                print(current_node.key, end=" ")

            if current_node:
                queue.append(current_node.lchild)
                queue.append(current_node.rchild)
    
    def inorder_with_appendingonlist(self):
        if self == None:
            return "^null"
        result = ["^", str(self.key)]
        result.append(self.lchild.inorder_with_appendingonlist())
        result.append(self.rchild.inorder_with_appendingonlist())
        return "".join(result)

    
    def delete(self,data,rootkey):
        if self.key == None:
            print("Tree is empty so Deletion cannot be done")
            return
        
        #Find the node to be deleted. Reach to the node.
        
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given node is not present")
        
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present in the tree")
        else:
            # three cases to be consider. 
            # if node has 0 childeren,1 children and 2 children
            # by this point, self has reached to the node to be delted.
            if self.lchild == None:
                
                temp = self.rchild
                # this if conditon if we want to delete the root node with one child node.
                # if we dont apply this if logic, then , code will not delete root node with child node.
                # if this conditon becomes true, then we are deleting the root node.
                if data == rootkey:
                    # to delete the root node we replace the root node with right child 
                    # ie copy the value of right child to root node value
                    # copy the left and right child value of right node to root node.
                    self.key = self.rchild.key
                    self.lchild = self.rchild.lchild
                    self.rchild = self.rchild.rchild
                    self.rchild = None
                    return

                self = None
                return temp
            
            if self.rchild == None:
                temp = self.lchild
                if data == rootkey:
                    # to delete the root node we replace the root node with left child 
                    # ie copy the value of left child to root node value
                    # copy the left and right child value of left node to root node.
                    self.key = self.lchild.key
                    self.lchild = self.lchild.lchild
                    self.rchild = self.lchild.rchild
                    self.lchild = None
                    return
                self = None
                return temp
             # now for the node who has two children
            # here i will take the smallest node from the right subtree
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
    
    def smallest(self):
        if root.key == None:
            print("Tree is empty")
            return
        if self.lchild:
            return self.lchild.smallest()
        else:
            print("node with smallest key is",self.key)
            return self.key
            
    def smallest_iteratively(self):
        current = self
        while current.lchild != None:
            current = current.lchild
        return current.data
    
    def greatest(self):
        if root.key == None:
            print("Tree is empty")
            return
        if self.rchild:
            return self.rchild.greatest()
        else:
            print("node with greatest ket is " , self.key)
            return self.key
            
    def smallest_iteratively(self):
        current = self
        while current.rchild != None:
            current = current.rchild
        return current.data
    
    def invertTree(self):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if self == None:
            return None
        # swap the two nodes.
        temp = self.lchild
        self.lchild = self.rchild
        self.rchild = temp
        #recursively swap the left and right nodes.
        self.lchild.invertTree()
        self.rchild.invertTree()
        # return the root node.
        return self

    
    def sumofnodes(self):
        if self == None:
            return 0
        left_sum = 0
        right_sum = 0
        if self.lchild:
            left_sum = self.lchild.sumofnodes()
        if self.rchild:
            right_sum = self.rchild.sumofnodes()
        return left_sum + right_sum + self.key
    


    
    




        
root = BST(4)
list1 = [2,71,3,6,9]
for i in list1:
    root.insert(i)
root.search(6)
print("preorder")
root.preorder()
print()
print("inorder")
root.inorder()
print()
print("postorder")
root.postorder()

print()
print("levelorder")
root.level_order()

print()
print("levelorder with Nulls")
root.level_order_withNull()

print()
print("inorder with node value appending on lists")
root.inorder_with_appendingonlist()
# root.delete(8,root.key)
# print()
# print("tree after deleting node") 
# root.inorder()
print()
root.smallest()
root.greatest()
# root.invertTree()
print("sum of nodes is " + str(root.sumofnodes()))