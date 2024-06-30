# leetcode: 75
#https://leetcode.com/problems/sort-colors/
# Arrays, two pointers, swapping.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        # one pass solution.
        # the idea is to take all 0's to left, all 2 on right.
        # left and right are two pointer and i is another pointer.
        # if nums[i] become 0, then swap it with left pointer and increment left and i.
        # if nums[i] == 2, swap it with right pointer becuasw we want to take 2 on right side and decrement right..
        # but here if nums[i] == 2, we do not incresae left pointer, it is in same position.
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                # negate i to make it in same position because later, i is going to increase and in this condition, we want i to be in same position.
                i -= 1



            elif nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1 
            i += 1
          
        return nums

     
        
        # 2 1 2 1 0 0
        #     i    r


        """
        Do not return anything, modify nums in-place instead.
        """
        # algorithm..
        
        #        swap 0 and 2 , ----- 0 comes ahead of 2.
        #        swap 0 and 1 ------- 0 comes ahead of 2.
        # and then swap 1 and 2. ---- 1 comes ahead of 2.


        # def swap (a , b):  
        #     # Here a represent that will be swapped right, and b represents swapped on left.
        #     # (1, 0) shows , 0 will come on left and 1 will go on right.
        #     i  = 0
        #     j = 0
        #     # i always look for a and j look for b.
        #     while j < len(nums) and i < len(nums):
        #         if nums[i] != a :
        #             i += 1
        #         elif nums[j] != b or j < i:
        #             j += 1
        #         elif nums[i] == a and nums[j] == b:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #             j += 1
        
        # swap (2, 0)
        # swap(1, 0)
        # swap(2, 1)
        # return nums

        # Time complexity - o(N)
        # Space comlexity - o(1)

    
                

        








