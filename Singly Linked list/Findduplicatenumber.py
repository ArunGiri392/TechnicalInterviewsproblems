class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            # moving one step at time--> similar to linked list
            slow = nums[slow]
            # moving two step at time ---> similart to linked list
            fast = nums[nums[fast]]

            if slow ==  fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
            