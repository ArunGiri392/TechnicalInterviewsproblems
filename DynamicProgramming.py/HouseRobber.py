class Solution:
    def rob(self, nums: List[int]) -> int:
        # what is the idea here???
        # at every house, there is two possiblity, either you can rob it or you cannot rob it.\
        
    #     lets take this example:
    #     2 , 7, 9,    3,    1
    #               position
    #    lets say i am position 3, then there is two choice, either i can rob or not rob it.
    #    if i rob it: then i cannot rob its adjacent house, so 
    #    total money = total money robbed up to (n- 2 ) house + current house. ie total money up to 7th house + currenthousemoney.

    #     if i do not rob it: then i can rob its adjacent house, so 
    #    total money = total money robbed up to (n- 1 ) house ie totalmoney up to 9th house, 
    #    and now becuase i wnat to loot the maximum money, i will take the maximum from this possibilty.

    #    money = max(total money up to (n-2) + money of current house,  totalmoney up to (n-1) house)

        #  for the first house, max amount of  money to be lotted is first house money itself.
        #  for second house, max amound of moeny to be looted is max (first, or second house) because we want to loot the maximum money.
        #  onwards, third house, we can use formula to calcualte. 

        #  the problem firstly, is done using memoization, using some list, to store, but it turns out that we just keep the two most recent data at time, 
        #  so variable is used.

        if len(nums) == 1:
            return nums[0]
        if  len(nums) == 2:
            return max( nums[0], nums[1])
        max_at_first = nums[0]
        max_at_second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = max_at_second
            max_at_second = max(nums[i] + max_at_first, max_at_second)
            max_at_first = temp
        return max_at_second



