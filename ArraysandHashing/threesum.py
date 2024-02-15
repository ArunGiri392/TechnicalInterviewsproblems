def threeSum(self, nums):
        
        # The idea here is to the sort the array at first.
        # and we know how to find the two sum in sorted array.
        # but here we need to find three sum.
        # so for every each element in list, we will do two sum for the remaining elements in list:
        # for example: lets say we have  sorted list = [1,2,3,4,5]
        # for 1, we do two sum in [2,3,4,5]
        # for 2, we do two sum in [3,4,5] and this can easily be done with pointers.
        # for uniqueness, we first store all possible answer in hashset, but list cannnot be stored there as list, so convert it into tuple
        # and store it, it will automatically remove the repeated list. and after than, iterate through them to produce final output.
        nums = sorted(nums)
        result = []
        hashset = set()
        for i in range(0,len(nums)-2):
            left = i + 1
            right = len(nums)-1

            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                if threesum == 0:
                    hashset.add(tuple([nums[i],nums[left],nums[right]]))
                    left += 1
                    right -= 1
                    
                elif threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
        print(hashset)
        for element in hashset:
            result.append(list(element))
        return result
    # time complexity == o(N2) BECAUSE for every element in list, we are doing two sum so o(n) * o(n)
    # space complexity = o(N) we are keeping the list of result.