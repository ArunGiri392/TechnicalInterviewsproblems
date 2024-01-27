# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
# time complexity - o(logn) where N is the no of nodes.
# space complexity - o(1)
# it is logn cause, if both nodes are present in the left side, than we even dont go to the right side and viceversa.
# that is at every iteration, we are leaving the half amount of nodes, which makes it log(n) solution.

# Time Complexity:
# Best and Average Case: O(log n)
# Worst Case: O(n)
# Space Complexity:
# Best and Average Case: O(log n)
# Worst Case: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # both on left side, both on right side, splits from certain point
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        