class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_smaller = [-1] * len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)

        
        prev_smaller = [-1] * len(heights)
        stack = []
        for i in range(0,len(heights)):
            while stack and  heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                prev_smaller[i] = stack[-1] 
            stack.append(i)
       

        maximum  = 0
        # The logic to keep if any index does not have next smaller, then it means, for that index, it can build a recantngle on its right side to all thw way rightmost(end). so set, nextsmaller to lengthof array.
        # # similarly, The logic to keep if any index does not have prev smaller, then it means, for that index, it can build a recantngle on its left side to first block . so set, prevsmaller to -1.
        # and due to this boundary, we will never get breath 0 or less than 0. so we do not have to manually chedck, if breath ever becomes 0 or less, because it will never be. 
        for i in range(len(heights)):
            if next_smaller[i] == -1:
                next_smaller[i] = n  # Set to length of array

            if prev_smaller[i] == -1:
                prev_smaller[i] = -1  # No change needed
            
            breath = abs(next_smaller[i] - prev_smaller[i]) - 1  # Adjust for offset
           
            area = heights[i] * breath
            maximum = max(maximum, area)
        return maximum
#        