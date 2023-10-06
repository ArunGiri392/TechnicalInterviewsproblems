# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
                return 
        if root.val == val:
            return root

        if root.val > val:
            root = self.searchBST(root.left,val)
        else:
            root = self.searchBST(root.right,val)
        return root




        # roots = []
        # def bfs(root,val):
        #     if root == None:
        #         return 
        #     if root.val == val:
        #         roots.append(root)
        #         return

        #     if root.val > val:
        #         bfs(root.left,val)
        #     else:
        #         bfs(root.right,val)
        # bfs(root,val)
        # if len(roots) == 0:
        #     return None
        # return roots[0]

            