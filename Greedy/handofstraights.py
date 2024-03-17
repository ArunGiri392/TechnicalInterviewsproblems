class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False
        
        
        # take the smallest first, and try to make pair with it.
        # if consequtive element is not present, return False.
        # to find the next smallest, use hashmap, while we pop from it.
        frequency = {}
        for card in hand:
            if card in frequency:
                 frequency[card] += 1
            else:
                frequency[card] = 1
        
        unique_hand = []
        for card in frequency:
            unique_hand.append(card)
        
        min_heap = unique_hand
        heapq.heapify(min_heap)

        # ifnd minimum first from min_heap.

        while min_heap:
            minimum = min_heap[0]
            counter = 0

            while counter != groupSize:
                next_number = minimum + counter
                if next_number not in frequency:
                    return False
                else:
                    frequency[next_number] -= 1
                    if frequency[next_number] == 0:
                        # we have to pop it.
                        # but if top of heap does  not matches this minimum + counter, return False.
                        if next_number != min_heap[0]:
                            return False
                        
                        heapq.heappop(min_heap)

                counter += 1
        return True


                
