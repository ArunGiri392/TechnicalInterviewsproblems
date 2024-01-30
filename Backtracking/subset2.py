class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        # sorting to bring repeated element together.
        # later it will help us on moving index(to avoid the repeated element)
        nums.sort()

        def dfs(index,array):

            # base case
            if index == len(nums):
                result.append(array.copy())
                return
            
            array.append(nums[index])
            dfs(index + 1, array)

            array.pop()
            # moving index to not include the repeated element.
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1

            dfs(index + 1, array)

        dfs(0, [])
        return result
