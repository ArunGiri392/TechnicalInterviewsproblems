class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = nums[i]
                    count = 1
        return candidate
        
#         The algorithm I described is known as the Boyer-Moore Majority Vote Algorithm. It's used to find the majority element in an array efficiently. Here's a step-by-step explanation of how it works:

# The algorithm starts by assuming the first element in the array as the "candidate" for the majority element and initializes a "count" variable to 1.

# It then iterates through the array from the second element to the end.

# For each element in the array:

# If the current element is equal to the "candidate," it increments the "count" by 1. This means we've found another occurrence of the same element.
# If the current element is different from the "candidate," it decrements the "count" by 1. This indicates that we've found an element that's different from the current candidate.
# If the "count" ever becomes 0, it means that we've balanced the count of occurrences of the current candidate with occurrences of other elements encountered so far. In this case, we update the "candidate" to the current element and reset the "count" to 1.

# After the iteration completes, the "candidate" variable will hold the majority element.

# The algorithm works because, by design, the majority element (an element that appears more than ⌊n / 2⌋ times) will always have a positive "count" at the end of the iteration, while other elements will not be able to cancel out its count due to the constraint that the majority element appears more frequently. Therefore, the "candidate" variable will correctly hold the majority element.

# This algorithm has a time complexity of O(N), where N is the length of the input array, and it uses only a constant amount of extra space (O(1)), making it efficient for solving the majority element problem.
        