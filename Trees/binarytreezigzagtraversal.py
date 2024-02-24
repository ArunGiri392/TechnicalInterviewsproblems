# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            current_result = []
            for i in range(0, len(queue)):
                current_node = queue.popleft()
                current_result.append(current_node.val)

               
                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)
            result.append(current_result)
        
        final_output = []
        for i in range(0, len(result)):
            if i % 2 == 1:
                final_output.append(self.reverse(result[i]))
            else:
                final_output.append(result[i])
        return final_output
         
        
    def reverse(self, list):
        left = 0
        right = len(list) - 1
        while left < right:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
        return list

        # Therefore, the overall time complexity is O(n + m), where n is the number of nodes in the binary tree and m is the total number of nodes at odd levels (i.e., the sum of the lengths of lists at odd levels).
      
        #   [15, 17]

        #   [[3],[9,20], [15,17] ]
                
        #     [9,20]
                
