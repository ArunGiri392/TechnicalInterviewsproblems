#Leetcode 448.
#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # idea.
        # for repeating numbers, make it negative sign.
        # if at end, if there are index that never becomes negative, that particular number is not present in the list.

        result = []
        for number in nums:
            number = abs(number)
            if nums[number - 1] < 0:
                continue
            else:
                nums[number - 1] = -1 * nums[number - 1]
        
     

        for i in range(0,len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
            
        return result

      