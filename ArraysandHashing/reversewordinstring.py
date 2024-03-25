class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s) - 1
        result = []

        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue
            start = i

            while i >= 0 and s[i] !=  " ":
                i -= 1
            result.append(s[i + 1 : start + 1])
            i -= 1
        return " ".join(result)
        