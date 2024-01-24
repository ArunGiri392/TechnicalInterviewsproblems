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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        elif subRoot == None and root != None:
            return True
        
        # at this point, we check if the root, starting at this root contains the subroot.
        # if yes, we immediately returns True.
        #if not, we recursively check on the left and right child.
        if self.isSameTree(root, subRoot):
            return True
        else:
            #recursively checking on the left and right child.
            left_side = self.isSubtree(root.left, subRoot)
            right_side = self.isSubtree(root.right, subRoot)
            return left_side or right_side

      



    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
         
         if root1 == None and root2 == None:
             return True
            
         elif root1 == None or root2 == None:
             return False
         
         elif root1.val != root2.val:
             return False
         
         else:
             left_side = self.isSameTree(root1.left, root2.left)
             right_side = self.isSameTree(root1.right, root2.right)
             return left_side and right_side
         

    # Time complexity --o(M * N) For each Node in the main tree(root), it potentially calls 'is same tree'. If the main tree has M nodes, in the worst case, we call 'is same Tree' M times. so time complexity at worst case is o(M * N)

    # space complexity - depends upon the recursion stack.
    # space complexity of 'is same tree' is o(N) in worst case (skewed tree)
    #space complexity of 'is subroot' is o(M) in worst case (skewed tree)
    # overall space complexty -- o(M + N) , M or N can be dropped.


         








