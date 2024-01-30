class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # this soln is utilizing the DFS traversal of the graph.
        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        number_of_islands = 0
        stack = []

        for i in range(0, rows):
            for j in range(0, columns):
                # IF THAt grid value is 1, it means it is island and also, we have not visisted this island before.
                if grid[i][j] == "1":
                    # this means we have got a new island.
                    number_of_islands += 1
                    # push that cell, into the stack for processing.
                    stack.append((i, j))

                    while stack:
                        # pop out the cell from the stack.
                        row, col = stack.pop()
                        grid[row][col] = "0" # mark it as visited
                        # up, down, left, right
                        neighbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

                        for neighbour in neighbours:
                            nr, nc = neighbour
                            # this condition is to make sure, we do not go out of bound for some cases.
                            if (nr >= 0 and nr < rows) and (nc >= 0 and nc < columns) and grid[nr][nc] == "1":
                                stack.append((nr, nc))
        return number_of_islands

                    







# using DFS recursively. 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(row, col):
            # basecase
            if row < 0 or col < 0 or row == ROWS or col == COLS or (row, col) in visited or grid[row][col] == "0":
                return 
            
            
            # adding this position in the visited list
            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        




        no_of_island = 0
        for row in range(0, ROWS):
            for col in range(0, COLS):
                # if it is land, and it has not been visited previously.
                if grid[row][col] == "1" and (row, col) not in visited:
                      dfs(row, col)
                      no_of_island += 1
                
            

        return no_of_island

# BFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            
            while queue:
              r, c = queue.popleft()
              neighbours = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c- 1)]
              for neighbour in neighbours:
                  nr , nc = neighbour
                  if (nr >= 0  and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == "1" and (nr, nc) not in visited):
                      queue.append((nr,nc))
                      visited.add((nr, nc))
        




        no_of_islands = 0
        for row in range(0, ROWS):
            for col in range(0, COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row,col)
                    no_of_islands += 1
        return no_of_islands

# Time complexity -- o(M * N) BECAUSE EACH CELL NEEDS TO BE VISITED AT LEAST ONCE. 
        # Space complexity --- o(M * N)
#         Space complexity is affected by two factor.
#         1) Recursion depth and Visted set.
#         In the worst case, the visited set could contain all the cells in grid,so size of set could be o(M * N)
#         similarly, The recursion call stack depth in the worst case can be as deep as the total number of cells in the grid (again, 

# O(mn) in the case of a grid filled entirely with land). This is because the DFS might need to explore each cell before backtracking.
# meaning, if the gird is all 1 ie
#  1 1 1 1 
#  1 1 1 1
#  1 1 1 1
#   and when DFS works, it at a point, have to explore all possibilties and at one point, the recursive stack could be as higher as o(M * N)
