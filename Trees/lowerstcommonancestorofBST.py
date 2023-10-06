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


