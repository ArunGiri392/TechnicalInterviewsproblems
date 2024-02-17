class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # logic here is:
        # lets take this numbers.
        #  1 1 2 2 3 3 4 4 
        #  then if do not have a single element and they just have pairs, it is guranteed that, the starting of that pairs, will always be even(including 0)

        #  1 1 2 2 3 3 4 4 
        #  0 1 2 3 4 5 6 7
         
        #  but whenever, a single elment comes in, it disrubtes this order such that, the index of the starting point of even number becomes odd.
        #  now, we coul duse this logic,
        #  when we calculate the mid, then firstly, we determine, whether that mid, is starting of even pair or ending, 
        #  this could be doing with simple logic, ie

        #   if nums[mid] != nums[mid - 1]: then starting point, is itself, mid else starting point is mid - 1.
        #   after having, starting point of the pair, we check if it is even or odd.
        #   if it is even, meaning there is no disruption created by that single element before that starting point, so we can omit left side, so left = mid + 1
        #   else:
        #       if it is odd, meaning the disruption has happened before, and we know that single element must be onleft side, not on right side. so right = mid -1 


        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                return nums[0]
            if mid == len(nums) - 1:
                return nums[-1]


            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
            if nums[mid] != nums[mid - 1]:
                # starting point of even point
                starting_point = mid
                if starting_point % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                starting_point = mid - 1
                if starting_point % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 1
        return nums[mid]