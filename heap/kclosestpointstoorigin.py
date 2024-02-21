import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []

        for co_ordinate in points:
            x = co_ordinate[0]
            y = co_ordinate[1]
            distance = math.sqrt(x*x + y*y)

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-1 * distance, co_ordinate) )

            else:
                distance_from_heap = -1 * max_heap[0][0]
                if distance < distance_from_heap:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-1 * distance, co_ordinate))

        result = []

        while max_heap:
            co_ordinate = heapq.heappop(max_heap)[1]
            result.append(co_ordinate)
        return result

# Time complexity - n * logk


