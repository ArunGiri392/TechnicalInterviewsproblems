class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(result, temp_set, nums, start):
            result_set.append(list(temp_set))
            for i in range(start, len(nums)):
                temp_set.append(nums[i])

                backtrack(result_set, temp_set, nums, i + 1)

                temp_set.pop()
        
        result_set = []
        temp_set = []
        backtrack(result_set, temp_set, nums, 0)
        return result_set
# TIme complexity -- (n * 2 ^n)
# space complexity -- o(n)