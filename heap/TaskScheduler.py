import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # using hash_map to count the frequency.

        frequency = {

        }

        for task in tasks:
            if task in frequency:
                 frequency[task] += 1
            else:
                frequency[task] = 1
        
        # adding in the heap - maxheap
        max_heap = []
        for frequency in frequency.values():
            max_heap.append(-1 * frequency)
        
        heapq.heapify(max_heap)
        
        queue = deque() # pairs of [-cnt, idleTime]
        time = 0
        
        while max_heap or queue:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1

                if count != 0:
                    #queue = [ count, next avaialble time]
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time


