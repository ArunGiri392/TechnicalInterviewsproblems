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

# without using the, hashset:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
       
       # Here are two main things to remember. 
       # we want to have the unique answer. 
       # so, for i, we do not want to have the same element twice meaning.

        # -1 -1 -1 0 1 2
        # for first -1,when i is there, we get answer as -1, -1 and 2 right. 
        # so on next case, another -1 comes in, so if we keep it, we will get same, -1,-1 and 2 right.
        # so the idea,is in first position(i), if we used -1, then on another case, we do not want to use -1,
        # and this can be checkted with,  if nums[i] == nums[i-1], then, we do not want to consider this case.

        # the other case. is
    #     -2 0,0,0,0,0,0,2 2,2 2, 2, 2
    # #    i l                       r
    # lets ssay our i is -2, and l = 0 and r = 2, then first answer is: -2, 0, 2,
    # then if we increase l and r, again l = 0 and r =2, we get same answer:  -2, 0, 2,
    # so this redundant right?
    # so even left and right should not be repeated.
    # so what we do is: while left is equal to previous left, we keep on increassing left:
    # while nums[left] == nums[left - 1] and left < right:
    #                         left += 1 

    # and we do not have to increase right pointer, because left will ultimately come in the next pointer, and again, sum is calcuated, and right gets updated accordingly.




        for i in range(0, len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[left] + nums[right] == 0:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                    
                    elif nums[i] + nums[left] + nums[right] > 0: 
                        right -= 1
                    else:
                        left += 1
        return result


    # #   0 1 1
    # #   0 0 0

    # # -2,0,0,2,2
    #   -2 0,0,0,0,0,0,2 2,2 2, 2, 2
    #    i             l      r


    


            
