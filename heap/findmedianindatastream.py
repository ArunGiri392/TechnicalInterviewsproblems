import heapq
class MedianFinder:

        # The code implements a MedianFinder class to find the median of a stream of numbers efficiently.
# It uses two heaps: a max heap (self.small) for numbers smaller than the median and a min heap (self.large) for numbers larger than the median.
# When a new number is added (addNum), it is initially added to self.small. The code then ensures that self.small contains numbers smaller than or equal to those in self.large.
# To maintain balance, the code adjusts the size of the heaps and may transfer elements between them.
# The findMedian function returns the median value based on the sizes of the heaps and the top elements of the heaps.
# This approach allows for efficient median calculations with time complexity close to O(log n), where n is the number of elements in the stream.

    def __init__(self):
        # we need two heaps, smaller heap and large heaps.
        # smaller heap is implemented as the max heap and the large heap is implemented as the min heap.
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        # here firstly, whenever add num gets called, we just add it to the smaller one by default.
        heapq.heappush(self.small,  -1 * num)

        # making sure every num small is <= every num in large.
        if (self.small and self.large and 
           -1 * self.small[0] > self.large[0]):
           val = -1 * heapq.heappop(self.small)
           heapq.heappush(self.large, val)
        
        # uneven size?
        # ie len smaller - len larger > 1.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #if len(larger) - len(smaller) > 1:
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)



    def findMedian(self) -> float:
        # three possibilites. either length of two heaps might be equal or smaller might be greater, or lareger might be greater.
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        elif len(self.large) > len(self.small):
            return self.large[0]
        return ( -1 * self.small[0] + self.large[0]) / 2.0
    
# Time complexity:
# addNum Operation (O(log n)):

# When a number is added using addNum, it is initially pushed onto self.small, which is a max heap.
# The code ensures that the max heap property is maintained.
# In the worst case, the code may need to transfer elements between self.small and self.large, which involves heap operations.
# These heap operations have a time complexity of O(log n), where n is the total number of elements seen so far.
# findMedian Operation (O(1)):

# The findMedian operation simply calculates the median based on the sizes of the two heaps and the top elements.
# It doesn't involve any additional heap operations or sorting.
# Therefore, it has a constant time complexity of O(1).

#       

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()