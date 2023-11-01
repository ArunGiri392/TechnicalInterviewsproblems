class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        i = 0
        # This calcualtes the odd palindromic substring.
        # for example " aaa"
        # this counts { a, aaa, a, a} count = 4 , all the palindrome with odd length
        while i < len(s):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if s[left] == s[right]:
                    result += 1
                left -= 1
                right += 1
            i += 1
        
        # this counts { aa, aa} count = 2 , all the palindrome with even length
        i = 0
        while i < len(s):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if s[left] == s[right]:
                    result += 1
                left -= 1
                right += 1
            i += 1
        
        return result

        # so total count = palindrome with odd length + palindrome with even length ie 4 + 2 = 6
        # Time complexity --- o(N^2)
# because for each character in string, we expand the window on the left and right side.
# in the worst case, if there is no palindrome, for each character, we would be expanding the window all the way to the left and right. ie iterating the whole string for each character, which causes the time complexity to be o(N^2).

# Space complexity -- o(1)

