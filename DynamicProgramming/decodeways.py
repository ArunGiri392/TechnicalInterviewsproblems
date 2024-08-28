class Solution:
    def numDecodings(self, s: str) -> int:
        # idea.
        # either i can take 1 element or two element.
        # if i take 1 element, and that one element is 0, then i cannot make proceed further because 0 Cannot be represented with letter as per question.
        # if i take 2 element, and that two element lets say 36 is greater than 26, then i cannot also take it.

           # to take 1 or 2 element, proceed index by 1 and 2.
           # if index ever reaches end, we found one way.

     
        # to take 1 or 2 element, proceed index by 1 and 2.
        # memoize the calcuate date to later use it.        dp = {}
        def dfs(index):
            if index >= len(s):
                return 1

            if s[index] == "0":
                return 0

            # looking in cached data.
            if index in dp:
                return dp[index]
            



            ways = dfs(index + 1)


            if index + 2 <= len(s) and int(s[index : index + 2]) <= 26:
                ways += dfs(index + 2)
            # caching 
            dp[index] = ways
            return ways
        return dfs(0)

        # Time complexity - o(N)
        # Space complexity - o(N)


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def dfs(index, string):
            if index >= len(s) :
                return 1
            
            if index in dp:
                return dp[index]
            
            take_one = 0
            if s[index] != "0" :
                take_one = dfs(index + 1, string + s[index])
            
            take_two = 0
            if s[index] != "0" and index + 2 <= len(s) and int(s[index : index + 2]) <= 26 :
                take_two = dfs(index + 2, string + s[index : index + 2 ] )
            
            dp[index] = take_one + take_two
            return dp[index]

        
        return dfs(0, "")