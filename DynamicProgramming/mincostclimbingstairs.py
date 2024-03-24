class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if i am at top, then i will not need, any  money so a = 0,
        # b is the last element of cost ,ie last staircase.

        # 10 15 20 top
        #        20   0

        # from 20, we need 20$ atleast to reach top. 
        # now, we can use these two previous values, to get how much will it take to reach end from 15?
        # but we want to minimize the cost right?
        # so, if i am in 15, i have to spend 15, then, i have two choices ,either take one step or two step.
        # i will just go,which will takes less amount 
        # so take min(20, 0) ie min(a,b)

        # so from 15, if i take, 1 step, it will cost me 15 + 20,
        # if i take 2 step, it will cost me 15 + 0, 
        # so taking minimum benefits me.
        # so keep on doint this, and at last, return the min of a and b.

        a = 0
        b = cost[-1]

        for i in range(len(cost)-2, -1, -1):
            temp = b
            b = cost[i] + min(a,b)
            a = temp
        return min(a, b)

        #Time complexity - o(N)
        #space complexity - o(1)


