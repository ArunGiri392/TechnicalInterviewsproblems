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