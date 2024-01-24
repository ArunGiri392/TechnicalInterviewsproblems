def isSameTree(self, root1, root2):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # using concept from level order algorithm

        queue = []
        # put both the roots in the queue.
        queue.append(root1)
        queue.append(root2)

        while queue:
            # pop out first and second element from the queue.
            # here first represents the node from the first tree and 
            # second represents the node from the second tree.
            first = queue.pop(0)
            second = queue.pop(0)

            # if both first and second are None, it means we dont do anything. just move forward.
            # so continue is the best here.
            if first == None and second == None:
                continue
            # if first is Null here and second is not meaning, they are not equaal so return False.
            elif first == None and second != None:
                return False
            elif second == None and first != None:
                return False
            # if their values are not equal , return None.
            elif first.val != second.val:
                return False
            # what we want to do here?
            # we want to compare the left of the first tree and left of second tree and also
            # right of first tree and right of second tree. 
            # for that , first append, left of first tree and right, 
            
            queue.append(first.left)
            queue.append(second.left)
            queue.append(first.right)
            queue.append(second.right)
        return True
# Time complexity - O(N) because we have to traverse all the Nodes where N is the no of nodes.
#The time complexity of this code is O(N), where N is the total number of nodes in the larger of the two input trees. This is because we are performing a breadth-first traversal of both trees simultaneously, visiting each node once.
# Space Complexity - o(N) because we in queue, at worst, we have to store N no of nodes.The space complexity of this code is also O(N), where N is the total number of nodes in the larger of the two input trees.

# recursive way of solving the problem

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val == root2.val:
            left_side = self.isSameTree(root1.left, root2.left)
            right_side = self.isSameTree(root1.right, root2.right)
            return left_side and right_side
        else:
            return False
# Time complextiy - O(N) where N is the number of nodes in each tree.
# Space complextiy - Height of the recrusion stack.
# for balanced tree- o(logN) where N is the number of Nodes in tree.
# for unbalanced tree - O(N) for example skewed tree.