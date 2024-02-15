import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -1 * stone)
        
        while max_heap:
            first_highest = -1 * heapq.heappop(max_heap)
            second_highest = -1  * heapq.heappop(max_heap)

            if first_highest > second_highest:
                difference = first_highest - second_highest
                heapq.heappush(max_heap, -1 * difference)
            if len(max_heap) == 1:
                return -1 * heapq.heappop(max_heap)
        return 0


# Time complexity - o(N * Logn)
# space complexity - O(N)