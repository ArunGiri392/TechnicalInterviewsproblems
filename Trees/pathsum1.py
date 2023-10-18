# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The idea here is to calcuate the sum from root to all leaf nodes and check if the sum is equal to the target sum.
# so we keep on going to the leaf node, and keep tracking of the sum we hav encountered thus far.
# when we reach to the leaf node, we check if sum is equal to target sum or not.
# then we have to also check for another leaf node, but we have already calcualte some sum right?
# so we can create another function, which would hold sum at every node level.

# this way , we can check sum up to all the leaf nodes.

# # THis question taught me one things. when we initially call, function and we know, at each recursive call, that function sotre the parameters, local variables value.

# so, first call is f(1, 5, 0) -- when function runs its current sum (local value variable) becomes 1.
# # remember,on next function, call, we are sending, the current sum variable.
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: 
        
        def dfs(root, targetsum, currentsum):

            if root == None:
                return False
            currentsum = currentsum + root.val
            if root.left == None and root.right == None:
                if currentsum == targetsum:
                     return True
                else:
                    return False
           
            left = dfs(root.left, targetsum, currentsum)
            right = dfs(root.right, targetsum, currentsum)
            return left or right
        
        result = dfs(root, targetSum, 0)
        return result