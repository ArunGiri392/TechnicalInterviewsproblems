# leetcode 1343
#https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# Fixed sliding window

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum (arr[0 : k])
        count = 0
        for i in range(0, len(arr) - k):
            average = total // k
            if average >= threshold:
                count += 1
            
            total = total - arr[i] + arr[i + k]
        
        if total // k  >= threshold:
            count += 1
        return count
    # Time comlexity - o(N)
    # Space complexity - o(1)

        # 1 2 3 4

            


        # # # arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
        # # 0, 4

        # # # 2 2 2 2 5 5 5 8
        # # #          i

        # #   total = 6 - 2 + 2  = 6 - 2 + 5 = 9 - 2 + 5 = 12 - 2 + 5 = 15 - 5 + 8 = 18



        # # constant window size equal to k.
        # #   2 +  2 + 2 == 6
        # #   6 - 2 + 2 = 6
        # #   6 - 2 + 5 = 9

        # 12 / 3
        # 12 // 3 