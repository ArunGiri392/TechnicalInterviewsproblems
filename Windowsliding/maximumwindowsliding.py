#leetcode 239.
#https://leetcode.com/problems/sliding-window-maximum/description/
# Montonic increasing stack and Sliding window.

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # The idea is to maintain a monotonic decreasing queue. 
        # and when we try to add new element, from right pointer,
        # while this element is greater thean what is on end of queue# b, pop those elements form pop.
        # if this element, is smaller, than, add it.
        # by the way, we are adding index.

        # one thing to remember is to: 
         # while the first index in queue has the maximum, it should also be part of the current window.
         # so the maximum index is smaller than left poiner, because left pointer is the left most side of our window, and it maximum index is less than it, it means the maximum is not withinwinow, so pop it from frontside.

        result = []
        q = collections.deque()
        left, right = 0, 0

        while right < len(nums):
            # if the maximum is out of our , current window.
            if q and left > q[0]:
                q.popleft()
            #maitaining monotonic decreasing queue.
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)

            # if left > q[0]:
            #     q.popleft()
            # window size if k, then take the  first element from queue, and add it.
            if (right - left + 1) == k:
                result.append(nums[q[0]])
                left += 1
            right += 1
        return result

            

            # [1,3,1,2,0,5] 
            #    l
            #        r


            #  [1 ]


        # 1, 3, -1, -3, 5, 3, 6, 7
        #                      r
        #                l
        
        # [4, 5]    ---- [3,3,5,5,]
        #  0 1 2  3  4 5 6 7

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        result = []
        left = 0
        for right in range(0, len(nums)):

            # if current element is greater than last element in queue.
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            queue.append(right)

            # if we increase left pointer and maximum if from the prevous left pointer, we remove that previous max from the queue.
            if left > queue[0]:
                queue.popleft()

            # if windowsize becomes equal to K.
            if (right - left + 1) == k:
                result.append(nums[queue[0]])
                left += 1
        return result




       