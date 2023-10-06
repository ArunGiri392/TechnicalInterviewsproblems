class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #sorted information will gurantee you some facts that it is always sorted.
        # so if we are able to find which  side is sorted ,then we can search our element on that sorted side, if target number is on that side, then we search on that side,else we search on that side.

        # sorted side could be on left or could be on right? so we have to first, figure out which side is sorted and hav eto write logic for both cases.
        # how to find which side is sorted?
        # if first element in the list, is smaller than the middle element, it means sorted side is left, because it follows the principle of sorted.
        # if not, the sorted side is on right side.

        # now if sorted side is on left side, we can see if our target is on that side, if it is on that side, look on that side, else look on the right side.
        # simialrly, if sorted side on right side, we can see if our target is on that side, if it is on that side, loon on that side, else look on the left side.

        # because we find the sorted side, we can leverage the power of side to gurantee that we are looking on the right side.


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # if this condition is true, that means my sorted array is on the left side, not right side.
                # lets say, sorted part is on left of mid, then our target could be on left side or right side.
                if target >= nums[left] and target <= nums[mid]:
                    # if this condition is true, meaning target is between left and mid (including both of them) we know it is on left side, so 
                    # we being right to mid - 1

                    right = mid - 1
                else:
                    # if that is not the case, it means the target is on right side, and we increment the left pointer.
                    left = mid + 1


            else:
                # else, sorted array is on right side, not on the left side.
                # same case here too.
                if target <= nums[right] and target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1




