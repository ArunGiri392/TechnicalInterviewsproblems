#Bruteforce soln.
# Time: o(2^n) , space: o(n) where n is the number of items.

def dfs(profit, weight, capacity):
    return dfs_helper(0,profit, weight,capacity)

def dfs_helper(index, profit, weight,capacity):
    if index == len(profit):
        return 0
    # skip item i, meaning do not take this option.
    max_profit = dfs_helper(index + 1, profit, weight, capacity)

    # include item i, meaning take this item.
    # if i do this, my profit will increase and my capacity decreases.
    new_capacity = capacity - weight[index]
    if new_capacity > 0:
       p =  profit[index] + dfs_helper(index + 1, profit, weight, new_capacity)
       max_profit = max(p, max_profit)
    return max_profit



#memoization solution using 2d grids.
# Time: o(n * m) , space: o(n * m) where n is the number of items and m is the integer capacity..

def dfs(profit, weight, capacity):
    N, M = len(profit), capacity
    cache = [[-1] *(M + 1)  for _ in range(N)]
    return dfs_helper(0,profit, weight,capacity)

def dfs_helper(index, profit, weight,capacity,cache):
    if index == len(profit):
        return 0
    if cache[index][capacity] != -1:
        return cache[index][capacity]
        
    # skip item i, meaning do not take this option.
    cache[index][capacity] = dfs_helper(index + 1, profit, weight, capacity)

    # include item i, meaning take this item.
    # if i do this, my profit will increase and my capacity decreases.
    new_capacity = capacity - weight[index]
    if new_capacity > 0:
       p =  profit[index] + dfs_helper(index + 1, profit, weight, new_capacity)
       cache[index][capacity]  = max(p,  cache[index][capacity])
    return  cache[index][capacity] 
