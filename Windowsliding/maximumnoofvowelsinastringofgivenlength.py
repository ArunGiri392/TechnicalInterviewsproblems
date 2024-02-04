class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        #
        # take first k elements
        # calculate their vowel count and maintain the maxium
        # looop throght to change the window size.

        # while looping, remove left most
        #      : if left most is vowel -
        #         decrease vowel count
        #         ele dont decrease
        
        # add the rightmost in window
        #    if it is vowel, 
        #        increase vowel couunt
            
        maximum = 0
        vowels  = "aeiou"
        vowel_count = 0
        max_vowel_count = 0

        hash_map = {}
        for i in range(0, k):
            if s[i] in vowels:
                vowel_count += 1

            if s[i] in hash_map:
                hash_map[s[i]] += 1
                
            else:
                hash_map[s[i]] = 1

        
        max_vowel_count = max(vowel_count, max_vowel_count)

        for i in range(0, len(s) - k):
             # remove the left most element from window.
            if s[i] in hash_map:
                if s[i] in vowels:
                    vowel_count -= 1
                hash_map[s[i]] -= 1
                if hash_map[s[i]] == 0:
                    del hash_map[s[i]]
            
            # to add on the hash_map
            if s[i + k] in hash_map:
                hash_map[s[i + k]] += 1
                
            else:
                hash_map[s[i + k]] = 1
            
            # increment vowel_count if added element in vowel.
            if s[i + k] in vowels:
                vowel_count += 1
            
            max_vowel_count = max(vowel_count, max_vowel_count)

        return max_vowel_count


# Time complexity - o(N)
# Space complextiy - o(N)
    
# i even do not have to create a hash_map. 
# two pointers will basically help here.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

      
            
        maximum = 0
        vowels  = "aeiou"
        vowel_count = 0
        max_vowel_count = 0
        left = 0

        for right in range(0, len(s)):
            if s[right] in vowels:
                vowel_count += 1
            
            if right - left + 1 == k:
                max_vowel_count = max(vowel_count, max_vowel_count)
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1
        return max_vowel_count


# Time complexity - o(N)
# Space complextiy - o(1)