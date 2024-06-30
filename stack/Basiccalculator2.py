# leetcode 227.
#https://leetcode.com/problems/basic-calculator-ii/description/
# Arrays, Stack, pointers

class Solution:
    def calculate(self, s: str) -> int:
        # algorithm.
        # if its a digit , capture it inside a while loop.
        # if its a non digit and not space, then , they must be sign among this: "+ - / *"
        # so if it is the case, set sign variable to them.

        # now if sign is +ve, append the number to stack with + sign.
        # if sign is -ve, append the number to stack with -ve sign.
        # if sign is * or /, then pop out the number from stack , so we get previosu number, and we get our current nubmer from value , so do operations on this. 




        stack = []
        i = 0
        sign  = "+"

        while i < len(s):

            if s[i].isdigit(): 
                value = 0
                while i < len(s) and s[i].isdigit():
                    value = value * 10 + int(s[i])
                    i = i + 1
                i -= 1
                
                
                if sign == "+":
                    stack.append(value)
                elif sign == "-":
                    stack.append(-1 * value)
                elif sign == "*":
                    a = stack.pop()
                    stack.append(a * value)
                elif sign == "/":
                    a = stack.pop()
                    # Here the question says, always trunacte towards 0.
                    # // always work such that it round up towards -ve infintiy. 
                    # 3//2--> 1.5 --> 1 it works perfectly fine for the positive. 1.5 is round up towards -ve infintiy . 
                    # -3//2 --> -1.5 ---> 2 (well, here according to question, we should have round up to 0, it -1.5 should have become -1. but // gives -2 as it rounds to negative infintiy.)

                    # so // does not work for negativy if we want to truncate towards negative.
                    # // to solve this. we use math.trunc. 
                    # Math. trunc returns integer part with our rounding up. so Math.trunc(4.9) --> 4, Math.trunc(-3.2) --> -3
                    # so here we / used to divide, as it does not round up and then use Math.trunc on the result.

                    stack.append(math.trunc(a / value))


            elif s[i] != " ":
                sign = s[i]
           
            
            i += 1


        sum = 0
        for number in stack:
            sum += int(number)
        return sum
    

    # Time complextiy - o(N)
    # Space complextiy - o(N)
