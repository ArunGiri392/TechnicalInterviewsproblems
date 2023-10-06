class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # this soln is utilizing the BFS traversal of the graph.
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

                    
# Time complexity - o(N * M) where N is the no of rows and M is the no of columns because the code visits the all rows and column atleast once.
# Space Complexity - Space used by stack. in a  worst case, where all the elements in the grid are 1, stack would contain every cell (i,j) might be pushed in the stack such space complexity is o(n*M) WEHRE where N is the no of rows and M is the no of columns


# this soln is using, BFS.
        def numIslands(self, grid):
      
       
            if len(grid) == 0:
                return 0
            
            rows = len(grid)
            columns = len(grid[0])
            number_of_islands = 0
            queue = deque()

            for i in range(0, rows):
                for j in range(0, columns):
                    # IF THAt grid value is 1, it means it is island and also, we have not visisted this island before.
                    if grid[i][j] == "1":
                        # this means we have got a new island.
                        number_of_islands += 1
                        # push that cell, into the stack for processing.
                        queue.append((i,j))

                        while queue:
                            # pop out the cell from the stack.
                            row, col = queue.popleft()
                            grid[row][col] = "0" # mark it as visited
                            # up, down, left, right
                            neighbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

                            for neighbour in neighbours:
                                nr, nc = neighbour
                                # this condition is to make sure, we do not go out of bound for some cases.
                                if (nr >= 0 and nr < rows) and (nc >= 0 and nc < columns) and grid[nr][nc] == "1":
                                    queue.append((nr,nc))
                                    
            return number_of_islands
