class Solution:
    def rob(self, nums: List[int]) -> int:
        # # The problem is very similar to house robber one.
        # # here i just need to decide wether i have to rob house 1 or rob house last. because,  i cannot rob them together. 
        # so, if i say, rob first house and not rob last house,  then, i will sendthe 0: n -1 (not last house) to my houserober function which is houserobber 1 and it gives the maximum i can rob.
        # simialrly, if i say, rob last house, and not first house, then , i will sendthe 1: n  (not first house) to my houserober function which is houserobber 1 and it gives the maximum i can rob.

        # so now i will calculate the maximum from thsese two cases and this will be my final respnse.
        if len(nums) == 1:
            return nums[0]
        if  len(nums) == 2:
            return max( nums[0], nums[1])
        
        def houserobberone(nums: List[int]):
            if len(nums) == 1:
                return nums[0]
            if  len(nums) == 2:
                return max( nums[0], nums[1])
            max_at_first = nums[0]
            max_at_second = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                temp = max_at_second
                max_at_second = max(nums[i] + max_at_first, max_at_second)
                max_at_first = temp
            return max_at_second
        
        includingfirstandexcludinglast = houserobberone(nums[0:len(nums)-1])
        includinglastandexcludingfirst = houserobberone(nums[1:])

        return max(includingfirstandexcludinglast,includinglastandexcludingfirst )
