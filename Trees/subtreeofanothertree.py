# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        fullTree = self.preorder(root)
        subTree =  self.preorder(subRoot)
        print(fullTree)
        print(subTree)
        return (subTree in fullTree)


        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

    def preorder(self,node):
        result = ["^"]
        
        def preorder_traversal(node):
            if node == None:
                result.append("#")
                result.append("^")
                return 
            result.append(str(node.val))
            result.append("^")
            preorder_traversal(node.left)
            preorder_traversal(node.right)
        preorder_traversal(node)
        return "".join(result)
