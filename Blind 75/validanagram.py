class Solution(object):
    def isAnagram(self, s, t):
       dict1 = {}
       dict2 = {}

       for element in s:
           if element not in dict1:
               dict1[element] = 1
           else:
               dict1[element] += 1
        
       for element in t:
           if element not in dict2:
               dict2[element] = 1
           else:
               dict2[element] += 1
       return dict1 == dict2