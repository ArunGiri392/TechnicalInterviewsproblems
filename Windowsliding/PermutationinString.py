class Solution:
    #fixed window size problem
    # could get bound error.
    # refering from geeksforgeeks article. 
    # https://www.geeksforgeeks.org/window-sliding-technique/

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        
        hash_map1 = {}
        for char in s1:
            if char in hash_map1:
                 hash_map1[char] += 1
            else:
                hash_map1[char] = 1
        
        hash_map2 = {}

        for i in range(0, len(s1)):
            if s2[i] in hash_map2:
                 hash_map2[s2[i]] += 1
            else:
                hash_map2[s2[i]] = 1
        
        if hash_map1 == hash_map2:
            return True

        if len(s1) == len(s2):
            return False
        
        # going only up to last k elements, not going out of bound.
        # i in range(0, k) where k is length of fixed window size.
        for i in range(0, len(s2) - len(s1)):
            # remove  left most
    
            
            # removing from left most part.
            # if it is there, then decrement by 1,
            # after decrementing, if value becomes 0, remove it.
            if s2[i] in hash_map2:
                hash_map2[s2[i]] -= 1
                if hash_map2[s2[i]] == 0:
                    del hash_map2[s2[i]]
                    
            # can also be wrriten like this,this segment of code.
            # hash_map2[s2[i]] -= 1
            # if hash_map2[s2[i]] == 0:
            #     del hash_map2[s2[i]]
            
            # adding from right most part.
            
            right_position = i + len(s1)
            if s2[right_position] in hash_map2:
                hash_map2[s2[right_position]] += 1
            else:
                hash_map2[s2[right_position]] = 1
            
            if hash_map1 == hash_map2:
                return True
        return False


  # Time complexity -- o(N * 26) for each iteration, we compare two hashmaps with length of 26 letters.
  # Space comlexity -- o(26) --- only 26 letters.
        
        
