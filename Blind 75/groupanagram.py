def groupAnagrams(strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
       

    #     already_seen = set()
    #     final_list = []
    #     for element in range(0,len(strs)):
    #         if strs[element] not in already_seen:
    #             if element == len(strs) -1:
    #                 list = []
    #                 list.append(strs[element])
    #                 final_list.append(list)
    #                 return final_list


    #             list = []
    #             list.append(strs[element])
    #             already_seen.add(strs[element])
    #             for value in range(element + 1, len(strs)):
    #                 if isAnagram(strs[element],strs[value]):
    #                     list.append(strs[value])
    #                     already_seen.add(strs[value])
    #             final_list.append(list)
    #     return final_list

# 
#def isAnagram( s, t):
#             dict1 = {}
#             dict2 = {}
            
#             for element in s:
#                 if element not in dict1:
#                     dict1[element] = 1
#                 else:
#                     dict1[element] += 1
        
#             for element in t:
#                 if element not in dict2:
#                     dict2[element] = 1
#                 else:
#                      dict2[element] += 1
#             return dict1 == dict2

       # This soln involves sorting each word  and keeping sorted word as key and real word as value in the list form
       # so, if they are anagram, their sort will have same value, so update in the dictionary.
       # and last, return the values.
        # dictionary = {}
        # for original_string in strs:
        #     sorted_string = ''.join(sorted(original_string))
        #     if sorted_string in dictionary:
        #         dictionary[sorted_string].append(original_string)
        #     else:
        #         dictionary[sorted_string] = [original_string]
        # return dictionary.values()


        # using anothersolution.
        # idea here is : because problem said that there will only be 26 characters w ecreate a list contains 26 0s
        # then , we calculate loop through each string and each letter, and update its position in the list.convert from 0 to 1
        # and convert it to tuple because list cannot be stored as key in dictionary as it is mutable and tuple is not mutable
        # so keep this list as key and keep corresponding word as value.
        # # so for next word, do same, and if they are anagram, we will get same list cause we will be updating same postiont.
        # and when added in dictionary, we add that as value
        # else, not.

        dictionary = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter)-ord('a')] += 1
            if tuple(count) not in dictionary:
                dictionary[tuple(count)] = [word]
            else:
                dictionary[tuple(count)].append(word)
        print(dictionary.values())
        return dictionary.values()

        #Time complexity - o(N * M) where N is the length of list and M is the length of each letter.
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))