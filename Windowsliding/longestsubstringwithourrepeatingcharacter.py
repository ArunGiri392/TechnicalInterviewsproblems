class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # The idea here is to use the window sliding concept. 
        # slide through the window and make a window, and check if they are unique or not. if they are , calcualte length and max length.
        # we can use hashset to store those letter to find out window is unique or not.
        # hashset will always keep the unique letters ie and window will always be unique.
        # if at any point, there is repetion, we increase the start such that we change the window and will also delete it from the hashset to update the window.

        start = 0
        max_length = 0
        hash_set = set()
        for i in range(len(s)):

            if s[i] in hash_set:
                while s[i] in hash_set:
                   
                    hash_set.remove(s[start])
                    start += 1

            hash_set.add(s[i])
            # i will on the end of window and start is at the begiining of window so we can calcuate the length from their difference , but start starts from 0, so we need to add 1 to make that calcualtion valid.

            length = i - start + 1
            max_length = max(length, max_length)

            # this is the real code, but some things are repeating. so i made this code shorter as can be found above.
            # if s[i] not in hash_set:
            #     hash_set.add(s[i])
            #     length = len(hash_set)
            #     max_length = max(length, max_length)
            # else:
            #     while s[i] in hash_set:
            #         start += 1
            #         hash_set.remove(s[i])
            #     hash_set.add(s[i])
            #     length = len(hash_set)
            #     max_length = max(length, max_length)

        return max_length


# Time complexity - o(N)
# Space complexity - o(N)
        