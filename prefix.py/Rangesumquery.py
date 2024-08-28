# leetcode 303.
#https://leetcode.com/problems/range-sum-query-immutable/description/
# prefix sum, hashmap.

class NumArray:

    def __init__(self, nums: List[int]):
        self.container = {}
        prefix_sum = 0
        for right in range(0, len(nums)):
            prefix_sum += nums[right]
            self.container[right] = prefix_sum
        


    def sumRange(self, left: int, right: int) -> int:
        full_sum = self.container[right]
        if left != 0:
            half_sum = self.container[left - 1]
        else:
            half_sum = 0
        return full_sum - half_sum
# Time complexity - O(1) for SumRange function
# Space complexity - o(N)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
 
#  {
#     0: 1
#     1 : 3
#     2: 5
#     3: 10
#     4: 15

#  }
#  1 2 3 4 5 6

#  l,r => (2, 4) => 12

#  (0, 4) - (0, 1)  => 15 - 3 = 12

