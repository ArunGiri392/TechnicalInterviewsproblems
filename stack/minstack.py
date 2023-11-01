class MinStack:

#    logic
    #  at every time , we add to the stack, we keep track of Minimum at each point in another stack. 
    # if our current value is smaller than the minimum recorded at stack, then, for this turn, we make current as smaller.
    # else:
    #     we choose the same element at top of stack as smallest.

    #     every time, we pop from stack , we also pop from the minimum

    def __init__(self):
        self.minimumateachpoint = []
        self.stack = []
        self.flag = True

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.minimumateachpoint == []:
             self.minimumateachpoint.append(val)

        else:
            if val < self.minimumateachpoint[-1]:
                self.minimumateachpoint.append(val)
            else:
                self.minimumateachpoint.append(self.minimumateachpoint[-1])

        

    def pop(self) -> None:
        self.minimumateachpoint.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimumateachpoint[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()