from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    #The idea here is to implement BFS to find the max depth of treee
    # Essentially, if you are able to find the level of the tree, that correspond to max depth.
    # so you take node, and see if it has children or not, if it has , that suggest next level.
    # so add it and continue the process until you reach to the last node, and such that you find the level.
    def maxDepth(self, root):
       if root == None:
           return 0
       level = 0
       #create a queue with adding a root ()
       queue = deque([root])
       # while the queue is not empty , keep continuing this process.
       # This way we can visit all the nodes.

       while queue:
           # the reason for using for loop is : 
        #    lets say: in level two, you had two nodes, then for two nodes, 
        #    we want to increase interval by 1 , not by 2, cause they will be in same level.
        #    so using for loop make sure that we process those two node and pop them out and 
        #    then increase the level after processing those two nodes.
           for i in range(0,len(queue)):
            #pop node from the queue.
            node = queue.popleft()
            # if node has left or right child, then add it. else, dont add it on queue.
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 

           level += 1
       return level

# Time comlexity -- o(n) at worst case, we will atleast travel all the node.
# Space complexity -- 

#  Recursive solution:
# The idea here is to find the depth right?
# and it basically, is the largest distance from root node to the farthest leaf.
# so, what can we do?
# calcualte the height of left subtree and right subtree, and see which is greater, 
# anyone which is greater, we will take that because we want to take max depth.
# and once we get greater add that with current node(ie 1) cause node is standing in level 1
# and this should be recursive and should occur in each level.

def maxDepth(self, root):
       if root == None:
           return 0

       leftheight = self.maxDepth(root.left)
       rightheight = self.maxDepth(root.right)

       myheight = max(leftheight, rightheight) + 1
       return myheight


