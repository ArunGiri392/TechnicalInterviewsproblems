# Matrix -DFS
# Count the unique paths from top left to the bottom right. A single 
# path may only move along 0's and can't visit the same cell more than once.

def dfs(grid, r,c , visit):
    ROWS = len(grid)
    COLS = len(grid[0])

    if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 1:
        return 0
    if r == ROWS - 1 or c == COLS  - 1:
        return 1
    
    count = 0
    visit.add((r,c))

    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r,c))
    return count




dfs(grid, 0, 0, set())

# Time complexity --
# Every position has 4 options of going to 4 directions.
# so time complexity -- 4 ^(N * m) where N = no of rows and M = no of columns.

# Memory compleixty -- at most at call stack, there would (N * M) CALLS
# OR THE HASHSET COULD AT WORST CASE HOLD, N *M CORRDINATES.


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # Mark as visited
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)

        return num_islands

# Example usage
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

solution = Solution()
print(solution.numIslands(grid1))  # Output: 1
print(solution.numIslands(grid2))  # Output: 3
