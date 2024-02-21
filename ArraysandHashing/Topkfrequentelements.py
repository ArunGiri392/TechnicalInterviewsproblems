class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # we can think of o(n2) solution, preety easily.
        # keep number as key, and value as repetition. 



        # concept from the bucket sorting.
        # keep number as key in dictionary and value as repition. 
        # lets take a list: nums = [1,1,1,2,2,2,3,3,4]
        # dictionary would look like: {
            # 1: 3,
            # 2: 3,
            # 3: 2,
            # 4: 1
        # }
        # lets assume we have a  list.
        # [                     ]
        #   0   1   2  3    4   5
        
        # this number 0 ,1 ,2,3, 4, 5  is the index in the list.
        # so what if we, take this index of the list as the repetion of number(dictionary value) , and we keep the number itself in the value at that index. ie 

        # [     [4] [3]  [1,2]        ]
        #   0   1    2      3     4   5

        #   ie this suggest, number that is repeated 1 time is 4, number that is repeated 2 time is 3 and number that is repeated 3 time is 1 and 2.
        #   becaiuse many number can be repeated same no of times, so they should be kept on the list.

        #   the benefit of this approach is the length of the list will be equal to n,
        #   because in the worst case, if all numbers are unique, we onlu need index len(list) + 1.
        #   + 1 because we also keep 0 index.

        #   # now, if we iterate through the back of the list, on index 5, we get element that is repeated 5 times,
        #   so if we continue from back, we will get the k elements. ie keep on going from back. 
        
        dictionary = {}
        for element in nums:
            if element in dictionary:
                dictionary[element] += 1
            else:
                dictionary[element] = 1
        
        # initialize a 2 d lsit.
        list = []
        for i in range(0,len(nums)  + 1):
            list.append([])
        print(list)

        for n, c in dictionary.items():
            list[c].append(n)
        result = []
        for element in range(len(list) -1, 0, -1):
            for value in list[element]:
                result.append(value)
                if len(result) == k:
                    return result
                    
# Time complexity - o(N) where N is the length of list.
# space complexity - o(N) because we create a 2d list that is equal to N.
                


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        frequency = {}

        for number in nums:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1

        # This will not work!
         # buckets = [[]] * (len(nums) + 1)
        # the reason is, 
      
        # When you create a list using the expression buckets = [[]] * (len(nums) + 1), you're creating a list where all elements are references to the same empty list. So when you modify one sublist, it affects all other sublists because they all reference the same object.

# To fix this issue, you need to create independent empty lists for each element of buckets. You can achieve this using a list comprehension or a loop to create the sublists:

# python
# Copy code
      
        buckets = []


        for i in range(0, len(nums) + 1):
            buckets.append([])
        
        for key in frequency:
            
            repetition = frequency[key]
            buckets[repetition].append(key)
       

        result = []
        for i in range(len(buckets) - 1, - 1, - 1):
            bucket = buckets[i]

            for number in bucket:
                if len(result) < k:
                    result.append(number)
        
        return result


        

