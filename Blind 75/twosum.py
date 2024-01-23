class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        counter = 0
        for number in nums:
            complement = target - number
            if complement in dictionary:
                return [counter, dictionary[complement]]
            else:
                dictionary[number] = counter
            counter += 1