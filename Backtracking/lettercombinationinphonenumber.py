class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(index, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for char in digitToChar[digits[index]]:
               
                dfs(index + 1, curStr + char) 
        if digits:
            dfs(0,"")
        return res
# Time complexity - - o(N * 4^n)
# There are some number which has 4 letter.
# in worst case, we could number like 9999--
# and at each position we have 4 choices. so 4^n.


# Total Work Done: At each level of the tree, we're doing work proportional to the length of the string at that point. Across all levels, this results in a total work of 

# part comes from the total number of nodes in the recursion tree, considering the branching factor of 4.
# The 
# �
# N part is due to the work done at each node, which is proportional to the length of the string being constructed.