import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {

        }

        min_heap = []
        # calculation the frequency of numbers.
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
         
        # now put the k elements in the heap.
        # after putting k elements, we take other elements, and if frequency of this elemetn is greater than the root of heap, then we pop it out and add this element. 
        # because we are implementing minimum heap and at certaing time there will only be k no of elements in the heap.
        # since this is min heap, element with the minimum frequency is in the root so we just compare the current element frequence with the root. 
  # we want to add the object ie tuple  object ie (frequency , number ) in the heap.
    # because the min heap is made on the basis of frequcney, so when we add object, we want to keep frequcney at first than the number, because heap takes the first element (ie freqeuncey ) as basis when it makes a min heap. 

        for num, frequency in dict.items():
            # if lenght of heap is smaller than k , we just add to heap.
            if len(min_heap) < k:
                heapq.heappush(min_heap, (frequency, num))
            else:
                if frequency > min_heap[0][0]:
                    # min_heap[0] gives root and its [0] gives it frequency.
                    # pop the minimum, and add the current.
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,(frequency, num))
        result = []
        # now at this time, we have the most k frequent elements in the heap. there are only k elements. so just add that number ro the final result.
        for heap in min_heap:
            result.append(heap[1])
        return result
        

# Time complexity =
# 1) To convert to freqeuency -- o(N)
# 2) because length of heap is k and for all items in the list, we do either pop or insert ie log operation that makes it: n * logk
# ie for each item in the list, we do logk operation
# 3) at last, we traverse through minheap which is of length k and so we traverse and do append ie o(k)

# so overall time complexity is n * logk.
        