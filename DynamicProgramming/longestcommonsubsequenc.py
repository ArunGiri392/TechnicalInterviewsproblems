# Dp on strings.
#https://leetcode.com/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp on strings.
        # There are two cases, either character is match or character is not matched.
        # here ,we need two index , which would walk in two different strings.

        # if character from first string at certain index is equal to character from another string as same index,
        # then that means, we atleast got a one common, so 1 and now incrase both the index to go forward on remaining indexes.

        # if character does not match, then may be have to increase index1 or index 2, so we do both and from both of them, we get the maximum length subsequence.
        N = len(text1)
        M = len(text2)
        cache = [[-1] * M for _ in range(N)]

        def dfs(index1, index2):
            if index1 == len(text1) or index2 == len(text2):
                return 0
            
            if cache[index1][index2] != -1:
                return cache[index1][index2]
            
            count = 0
            # if character matches.
            if text1[index1] == text2[index2]:
                count += 1 + dfs(index1 + 1, index2 + 1)
            else:
                # if characer does not matches, --> two calls, once time increase index1, another time increase index2.
                count += max(dfs(index1 + 1, index2), dfs(index1, index2 + 1))
            
            cache[index1][index2] = count
            return count
        return dfs(0,0)

# Time complexity -- o(N * M) where N is the length of text1 and M is the length of text2. (possible states)
# Space complexity -- o(N * M) CACHE DATA
