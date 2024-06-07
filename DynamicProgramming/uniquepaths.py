#leetcode:62
#https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        rows = m
        cols = n
        grid = []

        # creating a 2d array and initializing everything with 1.
        for i in range(0, m):
            result = []
            for j in range(0, n):
                result.append(1)
            grid.append(result)
        
        # adding up and left value for each index.
        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row-1][col] + grid[row][col-1]
        return grid[m-1][n-1]
        
        # ROWS = m
        # COLS = n
        # visited = set()

        # def dfs(row, col):
            

        #     if row < 0  or col < 0 or row == ROWS or col == COLS or (row,col) in visited:
        #         return 0
            
        #     if row == ROWS - 1 or col == COLS - 1:
        #         return 1

        #     visited.add((row, col))
        #     count = 0
        #     count += dfs(row, col + 1) 
        #     count += dfs(row + 1, col)

        #     visited.remove((row, col))
        #     return count
        



        # return dfs(0,0)
        

        # o( 2 ^n *M)