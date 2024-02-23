
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # reverse preorder.
        
        def dfs(root):
            nonlocal prev
            if root == None:
                return

            dfs(root.right)
            dfs(root.left)

            root.right = prev
            root.left = None
            prev = root
        prev = None
        dfs(root)
        



      
        # def preorder(root):
        #     if root == None:
        #         return 
            
        #     result.append(root)
        #     preorder(root.left)
        #     preorder(root.right)
        #     return

        # result = []
        # preorder(root)
        # if root:
        #     ROOT = result[0]
        # else:
        #     return []
        # temp = ROOT

        # for i in range(1, len(result)):
        #     next_root = result[i]
        #     temp.right = next_root
        #     temp.left = None
        #     temp = temp.right
        # return ROOT
