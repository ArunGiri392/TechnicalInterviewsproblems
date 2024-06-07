#  Leetcode : 543
#https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #idea
        # for each node, find its maximum on left side, and maximum on right side, and add them. do this for each node, and calcualte the maximum of all nodes.
        # if we go from top to bottom,we have to do same work for each node, resulting time complexity to be o(n**2)
        # so we go from bottom to top, and for each node, we calculate the maximum on leftside and right side and also calcuate the sum of left_side and right_side and keep track of maximum thus far with global variable.
        
        max_diameter = 0

        def dfs(root):
            nonlocal max_diameter
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            max_diameter = max(max_diameter, left + right)
            return 1 + max(left, right)
       
        
        dfs(root)
        return max_diameter

        # return self.max_diameter

# This solution is without using the Global variable and instead using local variable. 
# instead of just returning 1 + max(left, right), we also return the max_diamter from each node, so the calling node can use that value to compare. 
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      
        def dfs(root):
            
            if not root:
                return (0,0)
            
            left, max_from_left = dfs(root.left)
            right, max_from_right = dfs(root.right)
            max_diameter = max(max(max_from_left, max_from_right), left + right)



            return (1 + max(left, right), max_diameter)

        max1, max2 = dfs(root)
        return max2