# The idea here is:
# 
# def productExceptSelf(self, nums):
#         # idea here is  to calculate the product of right side of each element.
#         # similarly, we can calculate the product of left side of each element.
#         # once, we have the right side product of each element and same for left, we can use them to find the final answer.
         
#         #function to find the right side product of each element in list.start from last side.
#         i = len(nums) - 2
#         right_side_multiplication_holder = [1]
#         previous_right_multiplication = 1
#         while i >= 0:
#             new_right_side_multiplication = previous_right_multiplication * nums[i+1]
#             right_side_multiplication_holder.append(new_right_side_multiplication)
#             previous_right_multiplication = new_right_side_multiplication
#             i = i -1
#         #function to find the left side product of each element in list.start from first.
#         j = 1
#         left_side_multiplication_holder = [1]
#         previous_left_multiplication = 1
#         while j < len(nums):
#             new_left_side_multiplication = previous_left_multiplication * nums[j-1]
#             left_side_multiplication_holder.append(new_left_side_multiplication)
#             previous_left_multiplication = new_left_side_multiplication
#             j = j + 1
        
#         # now i have the list of right side and left side multiplication holder.
#         result_array = []
#         i = len(nums) - 1
#         j = 0
#         while j < len(nums):
#             result_array.append(right_side_multiplication_holder[i] * left_side_multiplication_holder[j])
#             i = i - 1
#             j = j + 1
#         return result_array


# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# the idea here is you are allowed to have a final list(ie one list)
# so what i can do is: i can keep the right side of product in that list first,
# and on second loop, iterate from left side, calcuate the left side product of that element and 
# # and now, we have left side product in our variable and right in array, and multiply them 
# and update that result in the list . do this for all, such that the list we had initially 
# that contained the right side product gets converted to the final answer.

def productExceptSelf(nums):
        # idea here is  to calculate the product of right side of each element.
        # similarly, we can calculate the product of left side of each element.
        # once, we have the right side product of each element and same for left, we can use them to find the final answer.
         
        #function to find the right side product of each element in list.start from last side.
        i = len(nums) - 2
        right_side_multiplication_holder = [1]
        previous_right_multiplication = 1
        while i >= 0:
            new_right_side_multiplication = previous_right_multiplication * nums[i+1]
            right_side_multiplication_holder.append(new_right_side_multiplication)
            previous_right_multiplication = new_right_side_multiplication
            i = i -1

        # here now , we calculate the left hand side product, and multiyply with right hand side product
        # already in list, and update the value in the same list.
        # because, there is no element in the left side of first element, have to handle cautiously.
        
        i = 0
        j = len(nums)-1
        left_side_product = 1
        while i < len(nums):
             if i == 0:
                  final_product = 1 * right_side_multiplication_holder[j]
                  right_side_multiplication_holder[j] = final_product
             else:
                  left_side_product = left_side_product * nums[i-1]
                  final_product = left_side_product * right_side_multiplication_holder[j]
                  right_side_multiplication_holder[j] = final_product
             i += 1
             j -= 1
        # reverse a list
        i = 0
        j = len(right_side_multiplication_holder) -1
        while i < j:
             temp = right_side_multiplication_holder[i]
             right_side_multiplication_holder[i] = right_side_multiplication_holder[j]
             right_side_multiplication_holder[j]  = temp
             i += 1
             j -= 1

        
        return right_side_multiplication_holder
nums = [1,2,3,4]
print(productExceptSelf(nums))