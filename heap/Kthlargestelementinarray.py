import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq is a min heap implementation in the python, so if we put any elements in heap, it will always be in the min heap.
        # so if we want to acheive max heap, then just send -number to heap, in that way we can achieve the max heap using heapq module.

        # To find the Kth largest element using a min heap, you can input the negative values of the elements into the heap. This effectively reverses the order of elements in the heap, making the largest element (in terms of its original value) at the root of the heap.

#         Using Negative Values:

# When we negate the values and insert them into the min heap, we create a max heap in terms of the original values. The largest original value becomes the smallest (most negative) value in the heap.
# As a result, when we pop elements from the min heap, we effectively retrieve the largest original values first, which is what we want to find the Kth largest element.

        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        #popping k no times
        for i in range(0, k-1):
            heapq.heappop(max_heap)

        # pop the root also use negative value, because originally we sent negative value.
        return -heapq.heappop(max_heap)

# Time complexity -
# To convert a list to max heap or min heap , it requires o(n) time complexity.
# then for poping out from heap, it takes o(logn) time complexity
# and we need to this k times such that the overall time complexity becomes o(N  + K logn)