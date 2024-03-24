class Solution:
    # similar to permutations of string.
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        freqp = {}
        for char in p:
            if char in freqp:
                 freqp[char] += 1
            else:
                freqp[char] = 1
        
        result = []

        window = {}

        for i in range(0, len(p)):
            char = s[i]
            if char in window:
                window[char] += 1
            else:
                window[char] = 1
        
        
        if freqp == window:
            result.append(0)
  

        for i in range(0, len(s) - len(p)):

    
            window[s[i]] -= 1
            if window[s[i]] == 0:
                del window[s[i]]
            
            to_be_added_char = s[i + len(p)]
            if to_be_added_char in window:
                 window[to_be_added_char] += 1
            else:
                window[to_be_added_char] = 1
            
            #  i represents the anagram of next pointer.
            if freqp == window:
                result.append(i + 1)
            

        return result
