class Solution:
    def longestPalindrome(self, s: str) -> str:
        # The palindormic substring length could be odd as well as even.

        result = ""
        max_length = 0
        # current_length = 0

        i = 0
        while i < len(s):
            # for the odd case
            left = i 
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length
                    result = s[left : right + 1]
                left -= 1
                right += 1
           


            # for the palindrome with length even
            left = i 
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length
                    result = s[left : right + 1]
                left -= 1
                right += 1

            i += 1

        return result

 # Time complexity --- o(N^2)
# because for each character in string, we expand the window on the left and right side.
# in the worst case, if there is no palindrome, for each character, we would be expanding the window all the way to the left and right. ie iterating the whole string for each character, which causes the time complexity to be o(N^2).

# Space complexity -- o(1)