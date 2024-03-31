class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # idea. 
#         Recursive Approach with Dictionary Matching: The solution involves recursively trying to match every word in the given dictionary (wordDict) with the beginning of the substring starting from the current index of the input string (s). If a word matches, the recursive function is called for the remaining part of the string, starting from the end of the matched word. This process continues until either the end of the string is reached (indicating a successful segmentation), or all possibilities are exhausted without finding a valid segmentation.

# Memoization to Avoid Redundant Computations: To optimize the solution and avoid re-computing the possibility of segmenting substrings that start from the same index, a memoization technique is employed. A dictionary (or hash map) is used to store and retrieve the results of whether the substring starting from a specific index can be segmented into words found in the dictionary. This significantly reduces the number of recursive calls, especially for inputs where many substrings cannot be segmented, thereby improving the algorithm's efficiency.

        dp = {}


        def dfs(index):

            # memoization code.
            if index in dp:
                return dp[index] # either returns True or False.

            # base case
            if index >= len(s):
                return True
        

            for word in wordDict:
                if index + len(word) <= len(s) and s[index : index + len(word)] == word:
                    if dfs(index + len(word)):
                        #memoizing the result
                        dp[index] = True
                        return True

            dp[index] = False
            return False


        

        return dfs(0)

        # Time complexity - With memoization, the time complexity of the solution is O(n * m * l), where n is the length of the input string s, m is the number of words in the dictionary, and l is the average length of the words in the dictionary. This accounts for iterating over each index in s, checking each word in the dictionary, and comparing characters to find matches. The use of memoization ensures that each index in the string is effectively processed only once, making the algorithm scalable and efficient for practical applications.



        # solution 2...
        # This is the bottom to top approach.(iterative solution)

        # idea.
#        Initialize a DP Array: Create a boolean DP array, dp, marking all positions as False, indicating it's initially not possible to form a word ending at each index from wordDict. Set dp[len(s)] to True as a base case, representing the end of the string where forming a word is trivially possible.

#        Iterate Backward Through the String: For each index i from the end of the string s to the beginning, check if any word from wordDict matches the substring starting at i. If a match is found and the DP array indicates that forming a word is possible from the end of this word, set dp[i] to True.

#         Check Result at Start of the String: The value at dp[0] will indicate whether the entire string s can be segmented into a sequence of words from wordDict. If dp[0] is True, the segmentation is possible.
       
        # # Idea.
        # for each index , we calculate whether we can get any word in worddict from there.
        # if we can get, we store the result in dp by saying that, for this index, we can surely get some word.
        # we continue this appraoch, and ends at index 0, and at end, if index is true, then it means, it is possible.

        # initally, we are saying from all the index, it is not possible to make any word, so all set to false.
        dp = [False] * (len(s) + 1)
        # This is a base case, here , we are saying, dp[s] which is the next character of last character, setting it to True.
        dp[len(s)] = True

        # coming from backward and from each point check, if we can get any words from there.
        for i in range(len(s)-1, -1, -1):
            # for that we itearete through the given words.
            for word in wordDict:
                # we can slice according to length of each word we are getting and if it true, it means, from this index, we can atleast get one word.
                if  i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    # so we set, dp[i] as true, by evaluating i + len(word) what was the result at i + len(word.)
                    dp[i] = dp[i + len(word)]
                # if through any words, at this index, we get, true, we can break it. because we already know from this possible , we can atleast get one word.
                if dp[i] == True:
                    break
        # atleast return dp[0]
        return dp[0]
        
        # Time complexity - o(len(s)) * len(wordDict) * o(l) for slicing
        # space compleixyt - o(N)