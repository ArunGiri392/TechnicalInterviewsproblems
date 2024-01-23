import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # length of max_heap is equal to the length of k.
        self.minheap = []

        for data in self.nums:
            if len(self.minheap) < k:
                heapq.heappush(self.minheap, data)
            else:
                if data > self.minheap[0]:
                    heapq.heappop(self.minheap)
                    heapq.heappush(self.minheap, data)
        
                    

                    

  

    def add(self, val: int) -> int:
        # making sure that the length of heap is equal to k at minimum.
        if len(self.minheap) < self.k:
                heapq.heappush(self.minheap, val)
       

        elif val > self.minheap[0]:
                    heapq.heappop(self.minheap)
                    heapq.heappush(self.minheap, val)

        return self.minheap[0]
       
# Time complexity : for push or pop, it takes logk time where k is the size of the heap. a
# and we do this for n times(if n times added ) so that makes time complexity to be o(n * logk)
# Your solution looks correct for finding the kth largest element in a stream using a min-heap. The time complexity of your code is O(n log k), where n is the number of elements in the stream and k is the parameter you passed during initialization.

# Let's break down the time complexity:

# Initializing the min-heap with the first k elements takes O(k * log k) time.

# For each subsequent element in the stream, you perform the following operations:

# If the heap size is less than k, you push the element onto the heap, which takes O(log k) time.
# If the heap size is already k, you pop the smallest element if the new element is larger and then push the new element onto the heap. Both of these operations take O(log k) time.
# You perform the above operations for each element in the stream, so for n elements, the total time complexity is O(n * log k).

# This is an efficient solution, especially when k is much smaller than n. Well done!



        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# [ 4, 5, 8, 2] k = 3
# first time - [4,5,8,2,3] -- 4
# s time - [4,5,8,2,3, 5] -- 5
# Thir time - [4,5,8,2,3, 5, 10] -- 5
# Fourth time - [4,5,8,2,3, 5, 10, 9] -- 8
# Fifth time - [4,5,8,2,3, 5, 10, 9, 4]  -- 8

# nlogn -- first case

# make a max heap -- which will have first, second, and third highest, and pick third highest each time from there???
