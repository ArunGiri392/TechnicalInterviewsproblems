# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []
       
        result = []
        queue = []
        final_result  = []
        queue.append(root)

        while queue:
            

            result = []
            for i in range(0,len(queue)):
                
                current_node =  queue.pop(0)
                result.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            final_result.append(result.pop())

        return final_result