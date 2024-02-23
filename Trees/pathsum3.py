class Solution:
    count = 0  # Global variable

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        
        self.count = 0  # Reset count for each call
        self.dfs(root, 0, targetSum)
        return self.count + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def dfs(self, root, current_sum, targetSum):
        if root is None:
            return

        current_sum += root.val
        if current_sum == targetSum:
            self.count += 1

        self.dfs(root.left, current_sum, targetSum)
        self.dfs(root.right, current_sum, targetSum)
# time complexity - o(N2)
        
