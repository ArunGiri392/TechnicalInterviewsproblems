class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def dfs(index,subseq):
            if index == len(nums):
                result.append(subseq.copy())
                return
    
            # include the current element.
            subseq.append(nums[index])
            dfs(index + 1, subseq)
            
            subseq.pop()# Backtrack to remove the current element
            # Not include the current element
            dfs(index + 1, subseq)


        dfs(0, [])
        return result
        # Time complexity -  o(2(^n))
