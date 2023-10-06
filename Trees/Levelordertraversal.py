# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = []
        queue.append(root)
        final_result = []
        while queue:
            nodes = []
            # here the for loop is required for each level.
            # when we do for i in range(len(queue))
            # lets say at that time length of queue is 2, so loop will iterate two times but as we can see, inside the loop, we keep on appending in the list, meaning the length of queue keeps on increasing . but does that change the iteration of for loop? No
            # because the length is calcualted first, and it is fixed how many iteration is should go, despite we appending another node in the queue inside the loop.
            for i in range(0,len(queue)):
                current_node = queue.pop(0)
                nodes.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            final_result.append(nodes)
        print(final_result)
        return final_result

# Time complexity - o(n)
# Space complexity - o(n)

        # The while loop runs for each level of the tree, and the for loop iterates through all nodes. Therefore, the overall time complexity is O(N), where N is the number of nodes in the binary tree.

#         The space complexity is primarily determined by the space used for the queue and final_result.
# The queue stores nodes at each level, and in the worst case, it can store all nodes in a level before moving to the next level. Therefore, in the worst case, the space used by the queue can be O(N).
# The final_result list stores the result, which also takes O(N) space in the worst case.
# Additionally, the nodes list is used to temporarily store node values at each level, and its space usage is proportional to the number of nodes at the current level.
# Therefore, the overall space complexity is also O(N) in the worst case.
# In summary, the time complexity of the code is O(N), and the space complexity is O(N), where N is the number of nodes in the binary tree.








