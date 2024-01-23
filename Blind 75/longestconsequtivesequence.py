class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hash_set = set()
        maximum = 1
        for number in nums:
            hash_set.add(number)
        
        for number in nums:
            if (number - 1) not in hash_set:
                # This marks the beginning of new queue.
                counter = 0
                while (number + counter) in hash_set:
                    counter += 1
                maximum = max(maximum, counter)

        return maximum
