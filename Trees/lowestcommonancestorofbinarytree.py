# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        


        # # if one of the number is in left subtree 
        # # and another number is in right subree from .
        # # than that node would be LCA.

        # if left_side and right _side both are true, meaning, p and q are present in leftside and right side, so we can say: that root is lca.
        # if one of the node is present in left side, and another is not present in rightside, return left side. 
        # if one of the node is present in right side, and another is not present in leftside, return rightside. 
        


     


        def dfs(root):
            if not root:
                return 
            
            if root == p or root == q:
                return root
            

            left_side = dfs(root.left)
            right_side = dfs(root.right)
            
            if left_side and right_side:
                return root
            
            if left_side:
                return left_side
            return right_side

            
        return dfs(root)
        
            