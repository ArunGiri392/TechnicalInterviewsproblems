class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0

        def recursion(x, n):
            if n == 1:
                return x
            result = recursion(x, n//2)
            # multiplying by same result, to double it.
            result = result * result
            # handling the odd case.
            if n % 2 == 1:
                return result * x
            return result
        
        result = recursion(x, abs(n))
        
        if n > 0:
            return result
        else:
            return 1 / result
        
        # Time compleixty - o(logn) - base 2, cause we are diving at each point.

    #    n =3, 
    #    n = 1


        
        # n = 10, 2 ^ 10--- 2 ^5
        # n = 5, 2 ^ 2 * 2 ^2 * 2
        # n = 2, -- 2   --- r = 2 * 2  = 4
        # n = 1

        # 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2

        # 2 ^ 10 = 2^5 * 2 ^ 5
        # 2^5 = 2^2 * 2^2 * 2^1
        # 2^2 = 2^1 * 2 ^1

       

       