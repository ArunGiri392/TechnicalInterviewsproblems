# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # firstly, look for the node to be deleted.
        if root == None:
            return None
        if root.val > key:
           root.left = self.deleteNode(root.left, key)
        elif root.val < key:
           root.right = self.deleteNode(root.right, key)

        else:
            # this means, we got to the node to be deleted.
          if root.left == None:
              return root.right
          elif root.right == None:
              return root.left
          else:
              # meaning there are two child nodes.
            #   find the minumum in the right sub tree.
              current = root.right
              while current.left != None:
                  current = current.left
              # at this point, we have capture the smallest node, so copy it on the node to be deleted.
              root.val = current.val
              # now after copying current nodes val with the root val, there are two nodes with same value, so we have to delete the curretn node from bst.
              root.right = self.deleteNode(root.right, current.val)
        return root