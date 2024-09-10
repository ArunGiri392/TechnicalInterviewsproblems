class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        # There are three choices , either take 1 digit or take 2 digit or three digit.
        if len(s) > 12:
            return []
        final_result = []
        def dfs(index, result):

            # because at max, we can only have 4.
            if len(result) > 4:
                return 
            
            if index >= len(s):
                if len(result) == 4:
                    final_result.append(".".join(result.copy()))
                return 
            
            # taking 1
            result.append(s[index])
            dfs(index + 1, result)
            result.pop()
            
            # taking 2
            # it should not start with 0, but could be "00"
            if (index + 2) <= len(s) and s[index] != '0':
                 result.append(s[index : index + 2 ])
                 dfs(index + 2, result)
                 result.pop()
            
            # taking 3
            # it should not start with 0, but could be "000"
            if (index + 3) <= len(s) and s[index] != '0' and int(s[index : index + 3 ]) <= 255 :
                result.append(s[index : index + 3])
                dfs(index + 3, result)
                result.pop()

        dfs(0, [])
        return final_result

        # Time complexity - o(3 ^n)
        # space complexity - o(N)
       

        


        # either i could take 1 or take 2 or take 3.