# leetcode 567. Permutaion in string.

# for this question, i traverse through s2 and kept left and right pointer,
#     and if s2[right] in s1, i incremented right and when length of window became length of s1, i returned true.
# does not work!!!!
# let s1 = "abcd" s2 = "aaaaaaaaaaaaa"
#         if s2[r] is always a and a is always present in s1,(hashmap i made), so i cant just check it, may be i have to decrement value of a in hashmap ,or do something.
# but directly checking does not work.




# LEETCODE 1838.

#  for right in range(0, len(nums)):
#             window_size = right - left + 1
#             total = total + nums[right]

            
#             while nums[right] * (window_size) > total + k :
#                 total -= nums[left]
#                 left += 1
#             length = right - left + 1
#             maximum = max(length, maximum)

# Here in my soln, i calcuated the window size
# and i use this window_size in my while loop condition
# and inside the while loop i increment the left pointer,
# meaning the window size has to change right??
# but because, inside while loop, i do not update window size,
# and in my while loop, my window size is always what i calcualted previously,
# so , this is a mistake.

# for that i could directly calcuate the window size in while loop, rather than
#     calcualting at first.

#   for right in range(0, len(nums)):
#             total = total + nums[right]

            
#             while nums[right] * (right - left + 1) > total + k :
#                 total -= nums[left]
#                 left += 1
#             length = right - left + 1
# #             maximum = max(length, maximum)
#     now, (right - left + 1) which is window size gets updated accordingly.
            