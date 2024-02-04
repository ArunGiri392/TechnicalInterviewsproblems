class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        # 1, 4, 8, 3
        #   l     r
        #  lets assume i am 8, meaning my right pointer is at 8.
        #  now from 1 and 4 i have to check whether 1 and 4 can become 8 or not, if they are then i could have 8,8,8,3 and my max would be 3.
        #  so instead of manually adding numbers on 1 and 4 to make it 8, we could do this,
    
        # if 1 and 4 would have to become 8 right, 
        # then i would have  8,8,8, 
        # so that is nums[r] * window size(right- left + 1)
        # that is 8 * 3 = 24, this is hypothetical,
        # we also keep track of total sum betwen this windeo ie 1 + 4 + 8 = 13 , now we have k, meaning we can incrase any number by k times
        # ie 8 + k 
        # so if my hypohthetical sum <= (total sum + k), then it is a valid window, 
        # ie nums[r] * window size(right- left + 1) <= totalsum of window + K
        # if it is not valid, meaning my k is too less, then i can increase my  left pointer. 

        nums.sort()
        left = 0
        length = 0
        total = 0
        maximum = 0
        right = 0

        for right in range(0, len(nums)):
            total = total + nums[right]


            while nums[right] * (right - left + 1) > total + k :
                total -= nums[left]
                left += 1
            length = right - left + 1
            maximum = max(length, maximum)
            
    
# Time complexity - o(N)



            # if nums[right] * window_size <= (total + k):
            #     length = right - left + 1
            #     maximum = max(length, maximum)
            
            # else:
            #     while nums[right] * window_size > (total + k) and left <= right:
            #         total = total - nums[left]
            #         left += 1

            #     length = right - left + 1
            #     maximum = max(length, maximum)
            
        return maximum


