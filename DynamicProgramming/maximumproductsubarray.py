class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # result = max(nums)
        # current_max = 1
        # current_min = 1

        # for n in nums:
        #     if n == 0:
        #         current_max = 1
        #         current_min = 1
        #         continue
            
        #     temp = n * current_max
        #     current_max = max(n * current_max, n, n * current_min)
        #     current_min = min(temp, n, n * current_min)
        #     result = max(result, current_max)
        # return result

        
       
        left_product = 1
        right_product = 1
        result = nums[0]
        for i in range(0 , len(nums)):
            if left_product == 0:
                left_product = 1
            if right_product == 0:
                right_product = 1
    
            left_product = left_product * nums[i]
            right_product = right_product * nums[len(nums) - i -1]
                
          
            
           
           
            result = max(left_product, right_product, result)
           
            
        return result
