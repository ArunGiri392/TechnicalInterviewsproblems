class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        if len(s) < len(t):
            return ""
        
        # count of T is constant so we calculate the count of T.
        countT = {}
        windowfors = {}
        # calculating the count of T.
        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1
        # Need means how many equal do we need, and have shows at current window, how many character have we meet:
        have = 0
        need = len(countT)

        # we want to keep track of length of window and left and right pointer, so initailizing result which keeps pointer and result lenght.
        result = [-1, -1]
        resultlen = float("infinity")

        left = 0
        for right  in range(0, len(s)):
            char = s[right]

            # coutnting the character and adding in the window dictionary. 
            if char in windowfors:
                 windowfors[char] += 1
            else:
                 windowfors[char] = 1
            # if that character count is equal to the count in CountT(ie s): it means we have one match. so we increase have
            if char in countT and windowfors[char] == countT[char]:
                have += 1
            # if have == need, means in the current dictionary, we have every character present in the S. so we can keep track of its length and left and right pointer as this is one possiblilty for the pointer.
            while have == need:
                # update our result.
                if (right - left + 1) < resultlen:
                    result = [left, right]
                    resultlen = right - left + 1
                # after calculating,we need to shift left pointer to the right side so remove that char from dictionary
                # now pop from the left side , ie left window
                windowfors[s[left]] -= 1

                # when we remove it, now character in window might not be what we are in countT. so we check and if they are not, decrement have by 1.
                if s[left] in countT and windowfors[s[left]] < countT[s[left]]:
                    have -= 1
                # move the left pointer.
                left += 1
        left , right = result

        if resultlen != (float("infinity")):
            return s[left: right + 1]

        else:
            return ""

# Time complexity - o(N)
# Space compleixtity = o(26)
