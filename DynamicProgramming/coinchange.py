class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # find out how much coin do we need to make a amount of 11.
        # to do that, lets do how much coin do we need to make a amount of 0, 1 , 2, 3, -- and so on.
        # in this way, we can use the previous values.
        if amount == 0:
            return 0
        dp = {0:0}
        # here dp suggest, to make 0 amount, we need 0 coins.
        # key = amount, value = coins

        for i in range(1, amount + 1):
            # goes from 1 to 11.
            # now for each amount, calcuate how many coins do we need.
            # here , we could take any coins. if coin <= amount. if greater, then we cannot take it.

            minimum_coins_needed = float("inf")
            for coin in coins:
                # if i take this coin, remaining amount would be amount - taken coin
                if coin <= i:
                    remaining_amount = i - coin
                    total_coins_needed = 1 + dp[remaining_amount]
                    minimum_coins_needed = min(minimum_coins_needed, total_coins_needed)

            dp[i] = minimum_coins_needed
            
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]
# Time complexity - o(amount) * o(Coins)
# space complexity - o(N)
