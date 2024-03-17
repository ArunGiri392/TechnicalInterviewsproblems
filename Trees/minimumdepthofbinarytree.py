
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # using BFS TRAVERSAL.
        queue = deque()
        queue.append(root)                                      
        level = 1
        while queue:
            for i in range(0, len(queue)):
                current_node = queue.popleft()

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)
                                 
                if not current_node.left and not current_node.right:
                    return level
            level += 1
        return level
