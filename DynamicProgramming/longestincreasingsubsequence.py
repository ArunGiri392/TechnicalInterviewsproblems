class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # idea.
#         Initialization: Start by creating an array LIS of the same length as the input array nums, initializing all elements to 1. This reflects that the minimum length of an increasing subsequence for any element, considered in isolation, is 1.

# Dynamic Programming: Iterate through the input array nums, for each element nums[i], compare it with all previous elements nums[j] (where j < i) to find all possible increasing subsequences that can end with nums[i].

# Updating the LIS Array: If nums[j] < nums[i], it indicates that nums[i] can extend the subsequence ending at nums[j]. Update LIS[i] to be the maximum of its current value and 1 + LIS[j], reflecting the length of the new longest subsequence ending at nums[i].

# Finding the Result: The length of the longest increasing subsequence in the entire array is the maximum value in the LIS array, as it stores the longest subsequence lengths ending at each index.

        # This array indicates the maximum subsequnce up until ith position.
        # initally, it is set to 1 because initially, the maximum subsequcne is 1 for all indexes.


        LIS = [1] * len(nums)

        for i in range(1, len(nums)):
            maximum = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    maximum = max(maximum, 1 + LIS[j])
            LIS[i] = maximum
        return max(LIS)
    
    # Time complexity - o(N^2)
    # Space complexity - o(N)