# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
    # do a inorder traversal and see if they are sorted, if they are : they are binary search tree, else not.
    # doing inorder traversal on bst will always give a sorted results.
    # keeping the nodes values in the list and then check if they are sorted or not.
        # if root = None:
        #     return 
       sorted_nodes = []
       def in_order_traversal(root):
           
           if root == None:
               return
           
           in_order_traversal(root.left)
           sorted_nodes.append(root.val)
           in_order_traversal(root.right)
       in_order_traversal(root)


       for i in range(1,len(sorted_nodes)):
           if sorted_nodes[i] <= sorted_nodes[i-1]:
               return False
       return True
       

# Time complexity - O(N) where N is the no of Nodes in the BST.
# Space complexity - (N)
# BECAUSE A CALL STACK TAKES A SPACE OF O(n) where n is the no of nodes, if tree is balanced binary tree, then i t is o(logn)
# but we are using list to store nodes so that makes space complexity, o(N)


class Solution(object):
    def isValidBST(self, root):
        def in_order_traversal(root, prev):
            if root is None:
                return True

            # Recursively traverse the left subtree
            if not in_order_traversal(root.left, prev):
                return False

            # Check if the current node's value is greater than the previous value
            if prev[0] is not None and root.val <= prev[0]:
                return False

            # Update the previous value
            prev[0] = root.val

            # Recursively traverse the right subtree
            return in_order_traversal(root.right, prev)

        prev = [None]  # Initialize prev as a list to hold a mutable value (previous node's value)

        return in_order_traversal(root, prev)
# this soln does not require the list to be made, as we compare with current node values with previous node values.
