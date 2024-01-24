class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #sorted information will gurantee you some facts that it is always sorted.

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # if this condition is true, that means my sorted array is on the left side, not right side.
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1


            else:
                # else, sorted array is on right side, not on the left side.
                if target <= nums[right] and target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



