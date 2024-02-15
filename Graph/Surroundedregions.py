class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # The idea is traverse all the borders.
        # if you find "O", do dfs from there and convert all the "O: to T(Temporary variable)
        # the dfs from bordering o will make sure that it goes on and marks all the O's in the grid connected to bordering O's as F.

        # now, after this, we iterate over the entire matrix and if we see any 0, we convert it into X becuase this Os are the surrounded regions.

        # at last we traverse through the, grid to convert all t (temporary variable) to O's.
 
        matrix = board

        ROWS = len(matrix)
        COLS = len(matrix[0])
        visited = set()


        def dfs(row, col):

            if row < 0 or col < 0 or row == ROWS or col == COLS or matrix[row][col] == "X" or (row, col) in visited :
                return
            
            visited.add((row, col))

            if matrix[row][col] == "O":
                matrix[row][col] = "T"


            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)






        # go from left to right.
        # go from right to left.

        for i in range(0, COLS):
            if matrix[0][i] == "O":
                dfs(0, i)
            if matrix[ROWS - 1][i] == "O":
                dfs(ROWS - 1, i)
        
        # go from top to bottom.
        # go from botoom to top
        for i in range(0, ROWS):
            if matrix[i][0] == "O":
                dfs(i, 0)
            if matrix[i][COLS - 1] == "O":
                dfs(i, COLS - 1)
        
       
        # converting Os to X
        for row in range(0, ROWS):
            for col in range(0, COLS):
                if matrix[row][col] == "O":
                    matrix[row][col] = "X"
        
        # converting T to 0's.
        for row in range(0, ROWS):
            for col in range(0, COLS):
                if matrix[row][col] == "T":
                    matrix[row][col] = "O"
        return matrix


    # Time complexity - o(M * N)
    #   because even the dfs will make sure that we only visit each cell only once.

    # space complexity -o(M * N)