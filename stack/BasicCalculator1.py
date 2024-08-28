# leetcode 224.
#https://leetcode.com/problems/basic-calculator/description/
# Arrays, Stack, pointers

class Solution:
    def calculate(self, s: str) -> int:
        # Four cases.
        # varaibles used!
        # Sum - to keep track of sum throughout the iteration.
        # value - to keep track of value of digits at certain time.
        # stack - to work with ( and ) brackets
        # sign = +1 or -1, for sign changing, initially we start with +1 denoting any number is positive.

        # algorithm.

        # 1st case.
        #if char is digit, loop until we get the whole digit length.

        # after we get the whole digit, multiply value with the sign value to get its actual sign (its sign is already stored in sign variable.)
        # reset sign to + 1.
        # update sum to add it.

        # 2nd case.
        # if char is opening bracket.

        # add the current sum to the stack.
        # add the current sign to stack. (ecause when we get the reseult from inside the bracket, we need to evaluate with this sign and current sum.)
        # update sign to 1. because, we are going inside the bracket.
        # udpate sum to be 0. (because inside brack we have to do independent evaluation.)

        #3rd case.
         #if char is opening bracket.

         # pop out sum
         # pop out sign.
         # multiply current sum with sign.
         # add with pop sum.

         # 4th case.
         # if char is - sign.
          # negate the sign, meaning multiply current sum with -1 to reverse its sign because -ve only changes sign. positive does not. 
        
          # because postive does not add or change any sing, so we avoid so we dont write case for it. 




        sum = 0
        sign = 1
        stack = []
        i = 0


        while i < len(s):
            # if character is digit.
            
            if s[i] in "0123456789":
                value = 0
                while i < len(s) and s[i] in "0123456789":
                    value = value * 10 + int(s[i])
                    i += 1
                # here above when loop terminates, i will be in the non digit character.
                # and later, in the end we are again increment i . so that will cause, some character here to be left.
                # so decrementing i to brings to its original position and when below i increases, it goes to actual position.
                i -= 1 # Adjust for extra increment in the loop
                value = value * sign
                sum += value
                sign = 1 # reset to positive.
            
            elif s[i] == "(":
                stack.append(sum)
                stack.append(sign)
                sign = 1
                sum = 0
            
            elif s[i] == ")":
                sum = sum * stack.pop() # popping out sign
                sum = sum + stack.pop() # popping out previous sum
            
            elif s[i] == "-":
                sign = sign * -1
            i += 1
        return sum
    
    # Time complexity - o(N)
    # Space complexity - o(1)






         