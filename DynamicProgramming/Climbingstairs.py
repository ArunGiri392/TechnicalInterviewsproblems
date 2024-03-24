class Solution:

    # The problem is a DP problem.
    # # so on every step, we take a decision either we take 1 step or a 2 step. and on subsequent steps, the same process happens.
    # and this brings us to recursion, further we also know, we can use memoization to store some calcuate subproblems to avoid redundant calculation andbring the time complexity to o(N) FROM O(2 TO THE POWER N).

    # # ADDITIONALLY, IF WE THINK LIKE, to reach to the final step,lets say,
    # you are on third step, then you have two possiblilty, either you can take 4th or 5 th step.
    # but lets assume, you already know in how many way can you reach to the final step from 4th or 5th step.
    # so you just take that values and add them so that from third step, you know how many ways are there to reach to final state.

    # lets consider , 5th step is a final state.
    # to reach final state ie 5th step from itself, thereis one way.
    # from second last step, 4th, you can reach final, there is one way.
    # but from second third step, ie 3rd step, there is 1 + 1 , ie 2 steps.
    # so we add previous results(fibonnaci sequence)
    # and we continue this process up to n - 1 times.

    # it turns out that , we can just make use of two variables iniitalized to 1 initially, and just keep them updating.
    def climbStairs(self, n: int) -> int:
        temp1 = 1
        temp2 = 1

        for i in range( n - 1):
            sum = temp1 + temp2
            temp = temp2
            temp2 = sum
            temp1 = temp
        return temp2

    
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1

        if n == 0:
            return 0
        
        if n == 1:
            return 1
            
        if n == 2:
            return a + b


        for i in range(0, n-1):
            temp = b
            b = a + b
            a = temp
        
        return b

#using memoization.
class Solution:
    def climbStairs(self, n: int) -> int:

        steps = {

        }
        def dfs(step):
            if step == n:
                return 1
            if step > n :
                return 0
            # memoization
            if step in steps:
                return steps[step]



            steps[step] = dfs(step + 1) + dfs(step + 2)
            return steps[step]
            
        

        return dfs(0)
