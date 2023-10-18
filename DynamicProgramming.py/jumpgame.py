# class Solution:
#     # Greeedy solution, 
#     what is the idea here?
#     at each index, i will tell what is the maximum i can go.
#     and i keep on doing it.
#     if at any point, my maximum reach becomes sucht that it becomes to equal to length of array - 1, ie i reach to the end that means, i reached end and i directly return True.

#     so at every iteration, i will calcualte the maximumreached, and i store the maximum of all maximum reached.
#     because, i want to store the maximum distance possible , and i just want to keep the maximum i could possibly reach.

#     if at point,my index value becomes greater than the maximum reach, that means, i cannot reach end. 
    

#     # some notes for me and the mistake that i did in this problem. 
#      if i > maximum_reached:
#                 return False

#             maximum_reached = max(maximum_reached,nums[i] + i )
#      this is the order to the solution, but initially i did this, 

    

#     maximum_reached = max(maximum_reached,nums[i] + i )

#     if i > maximum_reached:
#         return False
#     does this make any difference???
#     yes, lets consider this case, lets say,: 
#      3  2 1 0 4 is my array.
#      when i = 0, max value is 3.
#       when i = 1, max value is 3.
#        when i = 2, max value is 3.
#          when i = 3, max value is 3.
#         when i = 4, now,if we calcuate the max value before comparing then
#         max value becomes , 4 + 4 ie 8, and 
#          if i > maximum_reached:
#         return False
#         this condition becomes false, as max_reached is greater than i.
#         but wait this should not have had happened right?
#         this happened because we calculated before compareing, 
#         if we had compare before then when i = 4, then max value would still become 3 and i would have become 4 and upon comapring ,the condition would become true and return false

def canJump(self, nums: List[int]) -> bool:
        maximum_reached = 0
        for i in range(0 , len(nums)):
            if i > maximum_reached:
                return False

            maximum_reached = max(maximum_reached,nums[i] + i )
           #nums[i] + 1 because , nums[i] is its potential to jump and i is its current postiion.
            
            if maximum_reached >= len(nums) - 1:
                return True 
       
        #  dynamic programming solution. o (N2 solution)
        # The idea here was: if i am at last poistion,can i reach to the last poisiton, well ofcourse yes,
        # so whati will do, is from last, i will check if from this position i can reach end, and keep on stroing index and keep value as whether i can reach to end or not from that position (either True or false.)

        # then, from 2nd last step, i will check whether i can reach last or not, if yes, store it in hashmap (as true)
        # again, from 3rd last step, i will check can i reach to the 2nd last step, if yes, store true, else store false.
        # so we keep on this and reach to the first and if if is truw, we can reach end , else not.
        # Time complexity = o(N@)
        # dictionary = {
        #     len(nums)  -1 : True
        # }
        # for i in range(len(nums)- 2, -1, -1):
        #     # can i reach end from this index
        #     value = nums[i]
        #     while value != 0:
        #         if (i + value) in dictionary:
        #             if dictionary[i + value] == True:
        #                 dictionary [i] = True
        #                 break
        #         value -= 1
        #     else:
        #         dictionary [i] = False
        # return dictionary[0]
