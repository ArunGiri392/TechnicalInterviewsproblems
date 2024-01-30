

    # what is the idea here?
    # a rotten orange will rot other oranges in i unit of time (lets say 1 minute).
    # so we have to first figure out where are the rotten oranges preseent. and see on 1 min, how many oranges does this rot?
    # after 1 min, then the new oranges will rot other oranges and this will continue.
    # so BFS is the best option here rather than dfs.
    # firstly, we go through the matrix and find out the rotten oranges in index and keep them in the stack .
    # then , we also add time in it, initially 0.
    # so , from queue, we pop one rotten orange, and look at four directions, and make fresh oranges rotten,
    # if there i 0 ie it does not have orange, so we dont have to check it, 
    # also after making fresh orange(rotten,) we make it 2, to remember that this orange is rotten already.
    # when we do this, we add this new rotten orange to queue, (with its index and time increased by 1) because after  1 min, they have been rottten.
    # so we keep on doing this until the queue is empty.

    # so at last, ther could be scenario where itmight be impossible to rot some orange, so we iteate through the grid and if we see any 1, then we return - 1. else we return the hgihest time encoutnered so far.

    # Note.
    # because, we change the matrxi from 1 to 2, to keep track of rotten orange, we dont have to create hashset to keep track, which have already been rotten. matrxi itself helps us.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        ROWS = len(grid)
        COLS = len(grid[0])
        Time = 0
        queue = deque()
        fresh = 0

        for row in range(0, ROWS):
            for col in range(0, COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        if fresh == 0:
            return 0



        while fresh > 0 and queue:
            for i in range( 0, len(queue)):
                r, c = queue.popleft()
                neighbours = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c- 1)]
                for neighbour in neighbours:
                    nr, nc = neighbour
                    if nr >= 0  and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] != 0 and grid[nr][nc] != 2:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            Time += 1

          
        
        if fresh == 0:
            return Time
        return -1

        
        














        


      
