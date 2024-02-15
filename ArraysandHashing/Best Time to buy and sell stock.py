# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Brute force soln
# in this soln, we take each number as buying and compare it with all the possibilies and we do it for all other number.
def buyandsellstock(prices):
    max_profit = 0
    for buying in range(0,len(prices)-1):
        for selling in range(buying+1, len(prices)):
            if prices[buying] < prices[selling]:
                profit = prices[selling] - prices[buying]
                if profit > max_profit:
                    max_profit = profit
    return max_profit
print(buyandsellstock([7,6,4,3,1]))

#Time complexity = O(N^2)
#space complexity =o(1)

# idea 2
# reduced complexity
# 310, 315, 275, 295, 260, 270, 290, 230, 255, 250
# min  5    min  20   min   10  30   min  25   min

# We keep track of the minimum value we have encountered so far and we when we get the number greater than the minimum value we subtract them to get a 
# maximum profit. If the next number is smaller than the previous minimum number, we keep the number as the new minimum number.We also keep track of 
# the highest profit every time and we return it at the end.

# pseudocode
# if element is greater than min - calculate the profit and update the max profit 
# else:
#   update minimum
# return the max profit

def buy_and_sell_stock_once(list):
  minimum = list[0]
  max_profit = 0
  profit = 0
  for element in range(1, len(list)):
    if list[element] > minimum:
      profit = list[element] - minimum
      max_profit = max(max_profit,profit)
    else:
      minimum = list[element]
  return max_profit
#print(buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
# 
# # min = 2
# profit = 290 - 255 = 25
# max_profit = max(30, 25 )  = 30
# element = 260