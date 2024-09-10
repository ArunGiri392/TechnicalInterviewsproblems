class Solution:
    def candy(self, ratings: List[int]) -> int:

        # The idea is to do two pass: once from left to right and another from right to left.
        # it is better understood with the example:

        # # lets say we have a ratings in ascending order:
        # 1 2 3 4
        # # then initially, all of them will have  1  1  1 1 candies right. 
        # then from 2nd index, we can compare to its left neighbour and because it is sorted, no of candies it gets should be greater than the left neighbour so 
        # 1 2 3 4 are the candies each index should get:

        # # smilarly, if it is in descending order:
        # 4 3 2 1 
        # then going from left to right is not possible because lets say : everyone gets 1 1 1 1 initially.
        # so then, starting from index 1, when we comare: 3 is not greater than 4 so we do not know how much to allocoate to it?

        # but in descending order, if we look from right to left, and compare i with i + 1, and i > i + 1, we can determine it:

        # 4 3 2 1 are the candies each should get:

        # but we will not alawys have sorted right:
        # so what we will do is:
        # first go from left to right: and if i  > i - 1, then increase i by 1 as compared to i - 1
        # then go from right to left: if i > i + 1, then we might think just increae by 1 as compared to i + 1.
        # but that does not work because:

        # 1 3 4 2
        # candies initally = [ 1 1 1 1]
        # after left pass candies = [1 2 3 1]
        # and if we just increase by candies[i + 1] by 1, then we would get candies as = [1 2 2 1]
        # did you observe what happen?
        # where candies was already 3, we made it 2 becuase we did candies[3] ie 1 + 1, so we are decreasing right. and that distrubes the order.
        # rather, we should take the max of current position value and candies[i + 1] by 1,
        
        candies = [1] * len(ratings)
        # left to right.
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(len(ratings) - 2, -1 , -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)

  