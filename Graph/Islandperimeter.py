class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0
        for row in range(ROWS): 
            for col in range(COLS):
                if grid[row][col] == 1:
                    directions = [[row + 1, col], [row -  1, col], [row, col + 1] , [row, col - 1]]
                    for direction in directions:
                        nr = direction[0]
                        nc = direction[1]

                        if nr < 0 or nc < 0 or nr == ROWS or nc == COLS:
                            count += 1
                        
                        elif grid[nr][nc] == 0:
                            count += 1
        return count 
        