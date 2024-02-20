# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # here there are two base cases.
    # 1) if root1 == None and root2 == None:
    #         return None
    # both of the root are None, we return NOne.
    
    # if root1 == None or root2 == None:
    #         if root1 == None:
    #           return root2
    #         return root1
    # if One is null and other is not, 
    # then i am directly returning the other one, and it seems if i return,
    # then for node , i am further not going deep, but it turns out that we do not have to go,
    #     because we are already connecting everythig when we return root1 or root2.

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None and root2 == None:
            return None

        if root1 == None or root2 == None:
            if root1 == None:
              return root2
            return root1
            
        root = TreeNode(root1.val + root2.val)
        
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right  = self.mergeTrees(root1.right, root2.right)
        return root
