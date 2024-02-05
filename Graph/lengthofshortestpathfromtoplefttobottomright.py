# Q: Find the length of the shortest path from top left of the grid to the bottom right.
# # Matrix (2D Grid)
# grid = [[0, 0, 0, 0],
#         [1, 1, 0, 0],
#         [0, 0, 0, 1],
#         [0, 1, 0, 0]]

def bfs(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    queue = deque()
    visited = set()
    queue.append((0,0))
    visited.add((0,0))
    length = 0

    while queue:
        for i in range(0,len(queue)):
            r, c = queue.popleft()

            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbours = [(r + 1, c), (r-1,c), (r, c+1), (r, c - 1)]
            for neighbour in neighbours:
                nr, nc = neighbour
                if nr < 0 or nc < 0 or nr == ROWS or nc == ROWS or grid[nr][nc] == 1 or (nr, nc) in visited:
                    continue
                queue.append((nr, nc))
                visited.append((nr, nc))
        length += 1
    return length




