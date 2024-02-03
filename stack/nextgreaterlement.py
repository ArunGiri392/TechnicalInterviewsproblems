# using monotonic stack.

def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []
    for i in range(0,len(nums)):
        
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index]  = nums[i]

        stack.append(i)
    return result

nums = [73, 74, 75, 71, 69, 72, 76, 73]
print(next_greater_element(nums))