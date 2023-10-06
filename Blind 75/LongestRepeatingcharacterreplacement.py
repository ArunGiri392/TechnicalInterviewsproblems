class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # what is the idea here
        # for any window to be valid what is the condition, 
        # remember we have to calcuate the maximum substring, so letssay,
        # we have a string , ' a, b,a,c, a'
        # lets say we calculate the maximum occurence of any letter in this string ie a,
        # then what we know is total length of window is 5
        # so 5. - 3 gives us th e other non major elements, a.
        # so if we are able to convert this no n major elements to the a itself, then we can say, it is a vlaid window, else not.

        # so, if the legth of window at that time, - most(repeatd letter in that window) <= k, then we say, it is a valid window,
        # else , not.


        hash_map = {}
        left = 0
        right = 0
        max_length = 0
        # create a dictionary to store keys and values.
        while right < len(s):
            if s[right] not in hash_map:
                 hash_map[s[right]] = 1
            else:
                 hash_map[s[right]] += 1
            
            # now, if length of window - most repeated letter is smaller than k, than it is valid window.

            if ((right - left + 1) - self.most_repeated(hash_map)) <= k:
                length = sum(hash_map.values())
                max_length = max(length, max_length)
                right += 1
            else:
                # if not, it is not a valid windows.
                # why use while loop here??
                # remember , if we do not keep while loop here, then at this point, we get a new window right because we are decrementing the left pointer,
                # so we also have to check if this new window is valid or not , before doing anything else, so we keep on checking if this new window is valid
                # or not, if now, we increment count, if not, then only we increment the right pointer.
                while ((right-left + 1) - self.most_repeated(hash_map) > k):
                    hash_map[s[left]] -= 1
                    left += 1
                right += 1
        return max_length
            
    
    
    def most_repeated(self, hash_map):
        most_repeated = 0
        for key, value in hash_map.items():
            if value > most_repeated:
                most_repeated = value
        return most_repeated

            
# time complexity  - 0(N * 26) because for each letter, we traverse in the dictionary to find the majority  but we know dicitonary is only 26 length in worst case. so 
# space comlexity - 0(26)


