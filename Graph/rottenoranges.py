class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

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
    
        
        if len(grid) == 0:
            return 0
        rows = len(grid)
        column = len(grid[0])
        maximum_time = 0
        time = 0
        queue = []
        #hash_set = set()

        # now firstly i have to traverse through the 2d list and find out where are the 2's present
        # and add their indices in the queue.

        for row in range(rows):
            for col in range(column):
                if grid[row][col] == 2:
                    queue.append((row,col,time))
                    #hash_set.add((row,col))
        print(queue)

        while queue:
            row, col,time = queue.pop(0)
            print(row,col)
            # up, down, left, right
            maximum_time = max(time,maximum_time)
            #print(maximum_time)

            neighbours = [(row - 1, col),(row + 1, col),(row , col - 1),(row , col + 1)]
            for neighbour in neighbours:
                nr, nc = neighbour
                print(nr, nc)
                if( nr >= 0 and nr < rows) and (nc >= 0 and nc < column) and grid[nr][nc] == 1:
                    print("entered")
                    queue.append((nr,nc,time + 1))
                    grid[nr][nc] = 2
          

        
        for i in range(rows):
            for j in range(column):
                print(format(grid[i][j]))
            print("next row")

        for row in range(rows):
            for col in range(column):
                if grid[row][col] == 1:
                    return -1
        return  maximum_time


