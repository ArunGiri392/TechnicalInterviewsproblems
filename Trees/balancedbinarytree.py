# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    # The idea is for every node, we have to check whether it is balanced or not. so this basically introudces a recursion in a general.
    # Top to bottom apprach gives o(N2) soln because for every node, we would go down and calcualte its left subtree length, righsubtree length and find the difference.
    # so we would do this for every node, so that is repeated work and that makes a soln o N square.

    # go from bottom to down and it will only take the one iteration to complete , do everything and iterate over each nodes one.
    #so go to down , last node, cacluate its left subtree length, right subtree length and see if it a valid balcnced subtree or not.
    # once we figure out,we need to pass the height as wellas the resutl (whether this was balanced or not)
    # we want to pass our result to above, becuase if this is invalid, then we pass it such that on upper level, decisions can be made using and conditions.
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(root):
            if root == None:
                return (0,True)
            
            left_height, is_balanced_left = dfs(root.left)
            right_height, is_balanced_right = dfs(root.right)
            is_balanced_subtree = (is_balanced_left and is_balanced_right)

            return (1 + max(left_height , right_height), abs(left_height - right_height) <= 1 and is_balanced_subtree)
        
        height, boolean = dfs(root)
        return boolean


        