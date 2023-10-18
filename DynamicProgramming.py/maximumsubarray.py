class Solution:

    # Kadane's algorithm
    # AI notes


#     Kadane's algorithm is a well-known algorithm used for finding the maximum sum subarray within a given array of integers. It was developed by Jay Kadane in 1984 and is a widely used technique for solving this problem efficiently with a time complexity of O(n), where n is the number of elements in the array.

# The algorithm works by maintaining two variables as it traverses the array:

# max_so_far: This variable keeps track of the maximum sum subarray found so far while iterating through the array.

# max_ending_here: This variable keeps track of the maximum sum subarray that ends at the current element in the array.

# The algorithm iterates through the array from left to right, updating these variables as it goes. At each element arr[i], it makes the following decisions:

# It compares arr[i] with max_ending_here + arr[i]. If arr[i] is greater, it means starting a new subarray is more beneficial, so it sets max_ending_here to arr[i]. Otherwise, it adds arr[i] to max_ending_here.

# It then compares max_ending_here with max_so_far. If max_ending_here is greater, it updates max_so_far with the value of max_ending_here.

# By the end of the traversal, max_so_far will hold the maximum sum subarray. 



    #my notes.

    # basically, we find the maximum endings at each index. so lets say, we calculate the maximum endings at index 4, so maximum endings at 
    # index 4 suggest taht we have treid out all the possiblitly it subarray starting from index 0 to 4, index 1 to 4, index 2 to 4, index 3 to 4, and index 4 itself. so we know the maximum endings at each index which we will use for calculating next maximum endings.


    def maxSubArray(self, nums: List[int]) -> int:
        # intially, maximum endings and max so far are set to first index itself.
        # max so far, preserves the maximum sum subarray we have encountered thus far.

        maximum_ending_here = nums[0]
        maximum_so_far = nums[0]

        for i in range(1, len(nums)):
            # so to get maximum endings, either maximum ending could be the index value itself or the sum of previos maximum endings + current index
            maximum_ending_here = max(nums[i], maximum_ending_here + nums[i])
            # if at point, the maximumendinghere, becomes bigger than maxsofar,it signifies we have found the new maxsofar.
            maximum_so_far = max(maximum_ending_here, maximum_so_far)
        return maximum_so_far