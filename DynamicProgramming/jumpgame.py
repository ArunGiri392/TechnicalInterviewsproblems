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

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        maximum_reached = 0

        while index <= maximum_reached:
            if maximum_reached >= len(nums) - 1:
                return True

            maximum_reached = max(nums[index]+ index, maximum_reached)

            
            index += 1
        return False
