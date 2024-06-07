#leetcode: 442.
#problem link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # idea.
        # we can use original list and each index position should only belong to one number, not to another.
        # 4 3 2 7 8 2 3 1

        # 1 2 3 4 5 6 7 8 -- this should be in reality if it goes from 1 to N.
        # so for each number, negate its index position, ie negative sign means, that we have already seen that particular number.
        # later , if we get same number, and when we try to make chnages in its index, we we will see thta it is negative, meaning, it is repeated.
        # # we make it negative, because we will always have positive number, so - means that we have already seen that number previously.
        result = []
        for number in nums:
            number = abs(number)
            if nums[number-1] < 0:
                result.append(number)
            else:
                nums[number - 1] = -1 * (nums[number-1])

        return result

        # Time complexity - o(N)
        # Space complexity - o(1)

        
