#leetcode - 494
# https://leetcode.com/problems/target-sum/

# idea
# either take + or take -, then in process, keep track of sum, 
# if + is taken, add to sum.
# if - is taken, sub to sum.

# for caching, index and amount are two parameters changing, so cache them(index, amount) ie overlapping subproblems.


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(index, current_sum):
            if index == len(nums):
                if current_sum == target:
                    return 1
                return 0
            
            if (index, current_sum) in dp:
                return dp[(index, current_sum)]
            
            ways = 0
            # take positive
            ways += dfs(index + 1, current_sum + nums[index])

            # take negative
            ways += dfs(index + 1, current_sum - nums[index])
            dp[(index, current_sum)] = ways
            return ways

        return dfs(0, 0)

        # Time complexity - o(N) * o(T) where N is the number of elements in Nums(no of index too) and T is the total sum that could be possible.
        # Space complextiy - o(N * T) for caching.