class Solution:
    def jump(self, nums: List[int]) -> int:

        # BFS on single list.
        # 2 1 3 0 0 4 5

        # now from position, 2, first index, we can reach at 1 and on 3.so that is our 2nd range

        # 2  1 3 0 0 4 5
        #    l r l   r

        #    now from 1 and 3, we calcuate where we could reach maximum, and that would be next right pointer.
        #    and left would be right + 1, to create a next window.

        left = 0
        right = 0
        steps = 0

        while right < len(nums) - 1:
            farthest = 0

            for i in range(left, right + 1):
                farthest = max(farthest,i + nums[i] )
            
            left = right + 1
            right = farthest
            steps += 1
        return steps




        