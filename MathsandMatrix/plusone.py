class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0

        for num in digits:
            number = number * 10 + num

        number += 1

        nums = []
        while number > 0:
            remainder = number % 10
            nums.append(remainder)
            number = number // 10
        
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums
        