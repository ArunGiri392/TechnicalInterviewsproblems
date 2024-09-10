class Solution:
    # source : take you forward.
    #https://www.youtube.com/watch?v=w_KEocd__20

    # idea:
    # either the sum could be > 0 or could be < 0:
    # if any subarray has the sum < 0, starting a new subarray is better than extending a subarray that has a negative sum.

    # so if any point, subarray sum becomes less than 0, we set to 0.
    # if it is positive, we keep on updating the maximum sum thus far.

    def maxSubArray(self, nums: List[int]) -> int:
        total_sum = 0
        maximum_sum = float("-inf")
        for number in nums:
            total_sum += number 
            if total_sum < 0 :
                total_sum = 0
            else:
                maximum_sum = max(maximum_sum, total_sum)

        # for all the numbers negative case.
        if total_sum == 0:
            return max(nums)
        return maximum_sum
