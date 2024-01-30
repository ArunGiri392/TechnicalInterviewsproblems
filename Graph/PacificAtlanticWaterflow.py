class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()
        
        def dfs(row, col, visited, prevHeight):
            if (row < 0 or col < 0 or row == ROWS or col == COLS or (row, col)  in visited or heights[row][col] < prevHeight):
                return
            
            visited.add((row, col))


            dfs(row + 1, col,visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
        
        for c in range(0, COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(0, ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        result = []
        for row in range(0, ROWS):
            for col in range(0, COLS):
                    if (row, col) in pac and (row, col) in atl:
                        result.append((row,col))
        return result
                    
        
# Time complexity -- o(N * M)

