def sort(list):
    stack1 = []
    stack2 = []
    temp_list = []
    
    for number in list:
        while stack1 and number > stack1[-1]:
            helper(stack1, stack2, temp_list)
        stack1.append(number)
    
    while stack1:
        helper(stack1, stack2, temp_list)

    result = []
    while stack2:
        result.append(stack2.pop())
    return result

def helper(stack1, stack2, temp_list):
    number = stack1.pop()

    while stack2 and number > stack2[-1]:
        temp_list.append(stack2.pop())

    stack2.append(number)
    while temp_list:
        stack2.append(temp_list.pop())


print(sort([1,2,9,3,4,5,7,1]))
print(sort([2,3,1]))
print(sort([5,4,3,2,1]))
print(sort([1,1,1,1,1]))
print(sort([-1,-2,-3,-4,-5]))
print(sort([1,100,1000,24,-67]))