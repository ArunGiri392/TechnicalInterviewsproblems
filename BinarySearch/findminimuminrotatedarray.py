class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = float("infinity")
        while left <= right:
            mid = (left + right) // 2
            # if sorted array is in the left side.
            # take the smallest from the sorted array and because we took the smallest from that rotated array,
            # we can eliminate the sorted array and go to other side.
            if nums[left] <= nums[mid]:
                smallest = nums[left]
                minimum = min(minimum, smallest)
                left = mid + 1
            else:
                # if sorted array is in the right side.
                smallest = nums[mid]
                minimum = min(minimum, smallest)
                right = mid - 1

        return minimum

