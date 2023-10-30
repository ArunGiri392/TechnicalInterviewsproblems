# This problem solution helps in many other problem because it teaches how to handle the pointer on a certain cases.

def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  1 3 12 0 0
        #         i
        #             j 

        
        i = 0
        j = 0
        # #  i always look for 0, j always look for non 0.
        # so if nums[i] is not equal to 0, then increment i.
        # if nums[j] is 0 increment, and if j < i: then also increment j
        # why increase j, when j < i:
        # it is true that we do want to swap, but we only swap to take 0, to back . there should not be a case where we swap the 0 at back to front.
        # so we only kind of swap, when j > i.
        # so , want to make sure, j is front of i.

        while i < len(nums) and j < len(nums):
            if nums[i] != 0:
                i += 1
            elif nums[j] == 0 or j < i:
                j += 1
            elif nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        return nums
