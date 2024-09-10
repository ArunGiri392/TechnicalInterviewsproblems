# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        # The idea is:
        #  lets say we are at some node. X.
        # then , we want to find the maximum at that node, so it could pass from both left and right side,
        # so we cacluate the maximum from the left subtree, maximum from right subtree,
        # and we calcualte the sum of max(leftsubtree) + root.val + max(righsubtree), may be this could be maximum? 
        # or max(leftsubtree) + root.val may be the maxium. ?
        # or  max(rightsubtree) + root.val may be the maxium. ?$
        # or root itself, could be  maxium, as max of left and right subtree could be maximum.

        # logic implemented here.
        # maximum_sum = max(left_max + right_max + root.val, maximum_sum, root.val, root.val + left_max, root.val + right_max)

        # we keep maxium_sum as global variable to keep track.
        # now, we also need to get the max from left sutree and right subtree.
        # so we return max(leftside, rightside) + root.val, or root.val itself could be the maxium. so we take maximum of these case and return.

        # this logic implemented:
        #   return max(left_max + root.val, right_max + root.val,  root.val)

        maximum_sum = float("-inf")
        def dfs(root):
            nonlocal maximum_sum
            if not root:
                return 0
            

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            # we can get maximum from comparing
            # our current max, root.val + max from left, root.val + max from right , max from left + max from right + root.val or only root.
            maximum_sum = max(left_max + right_max + root.val, maximum_sum, root.val, root.val + left_max, root.val + right_max)

            return max(left_max + root.val, right_max + root.val,  root.val)
            #  return  max(max(left_max, right_max) + root.val, root.val)
        anser = dfs(root)
        
        return maximum_sum



      # Time complexity - o(N)
      # SPACE COMPLEXTIY - O(H) WHERE H IS THE HEIGHT OF THE BINARY TREE.

