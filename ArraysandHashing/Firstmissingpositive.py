#leetcode 41.
#https://leetcode.com/problems/first-missing-positive/
# manipulating existing array space, negating values, Maths.
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # using hashset.
        # keep all numbers in hashset, and iterate from 1 to len(nums) + 1 and if any is not present in hashset, we found our number.
        container = set()
        for number in nums:
            container.add(number)
        # The interesting question here is why are we iterating from 1 to len(nums) + 1?? right??
        # lets take an example: [1000,1001, 1002]
        # here the length is 3. so if the length of array is 3. because we look for minimum, we search for either 1 or 2 or 3 right??
        # so the best case wuld have been : [ 1, 2, 3]
        # so here, we look for 1, it is present, 2 and 3 and we decide okay, 4 is the one that is not present. ie len(nums) + 1.
        
        
        for i in range(1, len(nums) + 1):
            if i not in container:
                return i
        return len(nums) + 1

        # Time complexity - o(N)
        # Space complexity - O(N)



        # Another solution, with no space used.

        # This is a problem which motivates us to use the provided numbers . it is simialr to 1-n questions.where we negate numbers to make sure we have seen already.
        # so questions already gives us negative numbers, so make it 0. why 0? becasue, our answer could at minmum start form 1, so for that reason, for negative numbers, which are useless in our case, convert them to 0.
        # then traverse over original number, an dchange its index postion to -ve.
        # if number is 0 or greater than len(nums), we can ignore it  because they are out of bound of array.
        # then travel from 1 --len(array) and se eits respective index,and if it positive, ite means, originally this number was not there, that is why its index never became negative.

        # making negative numbers to 0.
        for i in range(0, len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # travel in each number
        for number in nums:
            real_number = abs(number)
            # if number is 0, or greatern then lenght of nums, or it is already negative, then we dont do anything.
            if real_number == 0 or real_number > len(nums) or nums[real_number -1 ] < 0 :
                continue

            elif nums[real_number - 1] > 0:
                nums[real_number - 1] = -1 * nums[real_number - 1] 
            
            # the reason of this part is: if we somehoww try to change 0 as - 1 * 0 , pyhton will make it 0. so we cannot make 0 to -0.
            # so for 0, we need a diffrent repsentation in negavtive, so for that ,we use: len(nums) + 1 here.
            elif nums[real_number - 1] == 0:
                nums[real_number - 1] = -1 * (len(nums) + 1)

           
           
           
        
        # traverse from 1 to len(nums) + 1
        for i in range(1, len(nums) + 1):
            # if any of them is positive, we found our answer.
            if nums[i-1] >= 0:
                return i 
        # after iterating through each number, inside loop, we never return means, we traverse everyuthing from 1 to len(nums) + 1 and everything is present inthe list.
        # so minimum should be len(nums) + 1, just the next number.
        return len(nums) + 1

        # Time complexity - o(N)
        # space complextiy - o(1)

        