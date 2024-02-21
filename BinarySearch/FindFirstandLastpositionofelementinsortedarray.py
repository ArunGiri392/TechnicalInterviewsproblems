class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
         # for first occurence,
        #    if nums[mid] is equal to target, then check its left, it left is different, then it is first occurence.
        #    if left is not same, then it is not first occurence, meaning, change right  pointer to mid - 1
        #    also, if nums[mid] becomes equal to target and mid == 0, then we could tell 0 is the first index, o is the first index.IndexError
           
        #    similar appraoch for finding the last occurence too.
        # searching for the first occurence.
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if mid == 0:
                    result.append(0)
                    break
                
                if nums[mid] != nums[mid - 1]:
                    result.append(mid)
                    break
                else:
                    right = mid - 1
                

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        print(result)
        # searching for last occurence.

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if mid == len(nums) -1 :
                    result.append(len(nums) - 1)
                    break
                
                if nums[mid] != nums[mid + 1]:
                    result.append(mid)
                    break
                else:
                    left = mid + 1
                

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if result:
            return result
        return [-1,-1]
