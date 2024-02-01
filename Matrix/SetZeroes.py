class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ROWS = len(matrix)
        COLS = len(matrix[0])

        # idea
        # firstly we do not travel thorugh first row and first column,
        # and start travelling from others.
        # then, on travelling,if any of them is zero, we set row 0 or col 0 to be 0.


        # after that, we again, travel on those remaining parts, and if row or col is zero, for that row and col, we set it to 0.
        # we also travel to check if row or col , contains 0, and set flag.

        # and late if flag == true, we make first row and first colum

        # traverse throiugh first row.
        row_zero = False
        col_zero = False

        for row in matrix[0]:
            if row == 0:
                row_zero = True
        
        for row in range(0, ROWS):
            if matrix[row][0] == 0:
                col_zero = True

            
        for row in range(1,ROWS):
            for col in range(1, COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1,ROWS):
            for col in range(1, COLS):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if row_zero:
            for col in range(0,COLS):
                matrix[0][col] = 0
        
        if col_zero:
            for row in range(0,ROWS):
                matrix[row][0] = 0
        return matrix





         


        

        