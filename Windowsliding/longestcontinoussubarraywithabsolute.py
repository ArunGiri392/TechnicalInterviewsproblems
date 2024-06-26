# leetcode 1438.
#https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
# Window sliding, two pointers, arrays, Deque, monontonic Deque.

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # with making helper functions.
        # Below is the code that solves problem without making helper function.

        # This problem is the variant of the maximum window sliding problem.
        # here we have to find the maximum element in any window as well as minimum in any window.
        
        def find_maximum(left, right, nums, max_queue):
            while max_queue and nums[right] > nums[max_queue[-1]]:
                max_queue.pop()

            max_queue.append(right)

            if left > max_queue[0]:
                max_queue.popleft()
            
            return nums[max_queue[0]]

        def find_minimum(left, right, nums, min_queue):
            while min_queue and nums[right] < nums[min_queue[-1]]:
                min_queue.pop()
            
            min_queue.append(right)

            if left > min_queue[0]:
                min_queue.popleft()
            
            return nums[min_queue[0]]



        maximum_length = 0
        
        left = 0
        max_queue = deque()
        min_queue = deque()
        for right in range(0, len(nums)):
            
            

            maximum = find_maximum(left, right, nums, max_queue)
            minimum = find_minimum(left, right, nums, min_queue)

            if abs(maximum - minimum) <= limit:
                length = right - left + 1
                maximum_length = max(maximum_length, length)
            else:
                left += 1
        
        

        return maximum_length

        # Time complexity - o(N)
        # Space compleixty - o(N)
        

        # without making helper functions
        maximum_length = 0
        left = 0
        max_queue = deque()
        min_queue = deque()
        for right in range(0, len(nums)):
            
            # for finding the maximum in the subarray. (Maximum window sliding problem)
            while max_queue and nums[right] > nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(right)
            if left > max_queue[0]:
                max_queue.popleft()
            
              # for finding the minimum in the subarray. 
            while min_queue and nums[right] < nums[min_queue[-1]]:
                 min_queue.pop()
            min_queue.append(right)

            if left > min_queue[0]:
                min_queue.popleft()
        

            maximum = nums[max_queue[0]]
            minimum = nums[min_queue[0]]

            if abs(maximum - minimum) <= limit:
                length = right - left + 1
                maximum_length = max(maximum_length, length)
            else:
                left += 1
        
        

        return maximum_length
        