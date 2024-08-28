# leetcode 560.
#https://leetcode.com/problems/subarray-sum-equals-k/?envType=study-plan-v2&envId=top-100-liked
# prefix sum, hashmap.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Idea.
        # The genral idea of solving with two loops even using prefix sum, will still yield o(N2) solution.
        # so we calcualte the prefix sum of each index .
        # then, we store each prefix sum and its frequency . meanng how many times have we seen that prefix sum ?

        # how would storing prefix sum help us?
        # if we have the previous prefix sum and if current_prefix_sum - k is already in our prefix sum, it means, this prefixsum - k is something we dont want
        # and if it already we have seen, we can remove it right to obtain another sum array that equals k . so becasue we have already stored it . we can just its frequence with count.

        # the edge case is : we store 0 prefix sum as its count 1 intially. because prefixsum - k sometime might yield 0, and its count is 1 in this case.
        
        prefix_sum = 0
        container = {0:1}
        count = 0
        for right in range(0, len(nums)):
            prefix_sum += nums[right]

            if prefix_sum - k in container:
                count += container[prefix_sum - k]
            
            if prefix_sum in container:
                container[prefix_sum] += 1
            else:
                container[prefix_sum] = 1
            

        return count 

        # Time complexity - o(N)
        # Space complexity - o(N)

    



        # Bruteforce solution.
        # Time complexity - o(N)
        # Space complexity 0 o(N * N) very bad space complextiy.

        # The bruteforce solution involves calculating sum of each subarray and this involes two loops resulting in o(N2 SOLUTION)

        # container = {}
        # current_sum = 0
        # count = 0



        # for right in range(0, len(nums)):
        #     current_sum += nums[right]
        #     if current_sum == k:
        #         count += 1
        #     container[(0, right)] = current_sum
        
        # for left in range(1, len(nums)):
        #     for right in range(left, len(nums)):
        #         current_window_sum = container[left - 1, right] - nums[left - 1]
        #         if current_window_sum == k:
        #             count += 1
        #         container[(left, right)] = current_window_sum
        # return count 

                
    #    1 1 1 
    #        l
    #        r

    #    {
    #     (0,0) -> 1
    #     (0, 1 ) : 2
    #     (0, 2 ) : 3
    #     (1,1) : 1
    #     (1,2) : 2
    #    }

    #    count = 1



        

        




        # {
        #  (0,0) --> 1
        # # (0,1) --->3
        # # (0,2) -->6
        # # (0,3) --->-1
        # # (0,4) -->6

        # }
        # cs = 3

        # # 1 2 3 -7 7
        #     l
        #         r

        #     3 - 1 = 2
        #     0, 2 = 6 - 1 
        #     0, 3 = 

        

        # # (0,0) --> 1
        # # (0,1) --->3
        # # (0,2) -->6
        # # (0,3) --->-1
        # # (0,4) -->6

        # # 1, 2 -- (0,2) - (0,0) = 5
        # # 1, 3 --> -2
        # # 1, 4 --> 5

        # # 2, 3 --> (1, 3)  - s[1] = -2 -2 = -4




  
        

