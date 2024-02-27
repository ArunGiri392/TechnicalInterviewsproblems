# using monotonic stack.

#code for next greater
def next_greater_elements(nums):
    result = [-1] * len(nums)
    stack = []
    for i in range(len(nums) - 1,  -1, -1):
        
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
           stack.pop()
        
        if stack:
            result[i] = nums[stack[-1]]

        stack.append(i)
    return result

nums = [73, 74, 75, 71, 69, 72, 76, 73]
print(next_greater_elements(nums))


#code for next smaller.
def next_smaller(heights):
    next_smaller = [0] * len(heights)
    stack = []
    for i in range(len(heights)-1, -1, -1):
        while stack and heights[stack[-1]] > heights[i]:
            stack.pop()
        
        if stack:
            next_smaller[i] = heights[stack[-1]] 
        stack.append(i)
    return next_smaller

nums = [73, 74, 75, 71, 69, 72, 76, 73]
print(next_smaller(nums))


#code for prev greater.
def prev_greater(heights):
    prev_greater = [0] * len(heights)
    stack = []
    for i in range(0,len(heights)):
        while stack and heights[i] > heights[stack[-1]]:
            stack.pop()
        
        if stack:
            prev_greater[i] = heights[stack[-1]] 
        stack.append(i)
    return prev_greater
nums = [73, 74, 75, 71, 69, 72, 76, 73]
print(prev_greater(nums))



#code for prev smaller.
def prev_smaller(heights):
    prev_smaller = [0] * len(heights)
    stack = []
    for i in range(0,len(heights)):
        while stack and  heights[stack[-1]] > heights[i]:
            stack.pop()
        
        if stack:
            prev_smaller[i] = heights[stack[-1]] 
        stack.append(i)
    return prev_smaller
nums = [73, 74, 75, 71, 69, 72, 76, 73]
print(prev_smaller(nums))
