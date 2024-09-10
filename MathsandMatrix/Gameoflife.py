class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 1 lives if 2 or 3 neighbours
          # else dies.
        
        # 0 lives if exactly 3 neighbour
        # else dies.

        
        # # rule
        # original      new    denote
        # 0             0        0
        # 0             1        3
        # 1             0        2
        # 1             1        1
        

        ROWS = len(board)
        COLS = len(board[0])
        for row in range(0, ROWS):
            for col in range(0, COLS):
                neighbour = self.count_neighbour(row, col, ROWS, COLS, board)
                if board[row][col] == 1:
                    if neighbour == 2 or neighbour == 3:
                        board[row][col] = 1
                    else:
                        board[row][col] = 2
                else:
                    if neighbour == 3:
                        board[row][col] = 3
                    else:
                        board[row][col] = 0
        # changing 2 to 0 and 3 to 1.
        for row in range(0, ROWS):
            for col in range(0, COLS):
                if board[row][col] == 2:
                    board[row][col] = 0
                elif board[row][col] == 3:
                    board[row][col] = 1
        return board
        
    def count_neighbour(self, r, c, ROWS, COLS, board):
        neighbours = [(r + 1, c), (r -1 , c), (r, c + 1), (r, c - 1), (r-1, c-1), (r-1, c + 1), (r + 1, c - 1), (r + 1, c +  1)]
        count = 0
        for neighbour in neighbours:
            (nr, nc) = neighbour
            if nr < 0 or nc < 0 or nr == ROWS or nc == COLS:
                continue
                # 1 reprsent originally it was 1 and 2 in matrix also reprsents originally it was 1.
            if board[nr][nc] == 1 or board[nr][nc] == 2:
                count += 1
        return count
    
    # Time complexity - o(M * N)
    # space complexity - o(1)
                