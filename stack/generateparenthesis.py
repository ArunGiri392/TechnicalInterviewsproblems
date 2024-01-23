class Solution:
    # backtracking problem.
    # at each step, we have two choice, either to take opening bracket and closing bracket. 
    # there are some conditions to take opening or closing bracket.
    # we take opening bracket, if count of opening bracket as of now is less than n.
    # we take clsoing bracket, if count of closing bracket as of now is less than n and count of closing bracket < count of opening bracket.

    # because if count of opening and closing are equal, then we cannot add the closing at that time.

    #Base condition
    # if at any point opening bracket == N and closing bracket == N, it means we hav used all opening and closing bracket and we got one of the possibility.
    
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(open, close, stack, n):

            if open == n and  close == n:
                result.append("".join(stack))
                return 


            # to add the opening brackets
            if open < n:
                stack.append("(")
                backtrack(open + 1, close, stack, n)
                stack.pop()

            # to add the closing brackets
            if close < n and close < open:
                stack.append(")")
                backtrack(open, close + 1, stack, n)
                stack.pop()
            
        backtrack(0, 0, stack, n)
        return result


