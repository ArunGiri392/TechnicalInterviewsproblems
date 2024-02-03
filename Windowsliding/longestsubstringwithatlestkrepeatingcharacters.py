
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        frequency = {

        }

        for char in s:
            if char in frequency:
                 frequency[char] += 1
            else:
                frequency[char] = 1
        
        hash_map = {}

        left = 0
        length = 0
        maximum = 0
        for right in range(0, len(s)):

            # add letter to the hashmap.

            if s[right] in hash_map:
                  hash_map[s[right]] += 1
            else:
                hash_map[s[right]] = 1


            if frequency[s[right]] < k:
                while left != right:
                    left += 1
                hash_map = {}

            if self.is_window_valid(hash_map, k):
                print(self.is_window_valid(hash_map, k))
                # print(left)
                # print(right)
                length = sum(hash_map.values())
                maximum = max(length, maximum)

            
                # increment the right pointer.
        return maximum
    
    def is_window_valid(self,hash_map,k):
        if not hash_map:
            return False
        
        for char in hash_map:
            print(hash_map)
            if hash_map[char] < k:
                return False
        return True
    

        




        # longest substring -- atleast K repeating characters.


        # a a a b b  k = 3

        # a a a b b b   k - 3 

        # a b a b b c   k = 2

        # a b a b b b   k = 2

        # a a b e b d c     k = 2

        # l
        #          r


        # {
        # #     a: 2
        #       b: 2
        #       d: 1
        #       c: 1
              


        # # }

        # {
        #     a: 2
        #     b:1
        # }

        # hash_map = {}
        # left = 0
        # maximum = 0
        # for right in range(0, len(s)):

        #     if s[right] in hash_map:
        #          hash_map[s[right]] += 1

        #     else:
        #         hash_map[s[right]] = 1
            
        #     # if my window valid???
        #     if is_window:
        #         length = right - left + 1
        #         maximum = max(length, maximum)
        #         right += 1
                
        #     else:

        #         # remove the left side 
        #         hash_map[s[left]] -= 1


                



