class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        # a grid starting from 1, can never reach to end.
        if grid[0][0] == 1:
            return -1

        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        length = 0

        while queue:
            for i in range(0, len(queue)):
                r, c = queue.popleft()
                
                if r == ROWS - 1 and c == COLS - 1:
                    return length + 1

                neighbours = [(r + 1, c), (r -1 , c), (r, c + 1), (r, c - 1), (r-1, c-1), (r-1, c + 1), (r + 1, c - 1), (r + 1, c +  1)]
                for neighbour in neighbours:
                    nr, nc = neighbour
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
       
        return -1 
# Time complexity - o(N * M)
# Space complexity - o(N * M)