class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
#         The idea of using constant space comes from the idea of using some space, and narrowing it down to the constant space. 
#         lets suppose we have matrix:
#            [y  y   N  ]
#        [ y  1  0  1
#          y  1  0  1
#         ]y  0  1  1

#         lets say we have two array: the first array, keeps track of whether that certain columns needs to be 0 or not, similarly, in another array, we keep track of whether certain array needs to be 0 or not. 
# then, after this when we know which column needs to be 0 and which column needs to be true, we could just do it turn by turn, to obtain the final answer.

# withouy using any space. 
# what if we used the first row and the first column as a space itself. 
# each element in the first row says, whether that particular column needs to be 0 or not
# similarly, each element in the first columnn, says, whther particlular row needs to be 0 or not.

# for the first row, ther is an intersection, so we create a seperate variable.
# the sepeprate varialbe will track of whether the first row needs to be 0 or not.
# whereas matrix[0][0] keeps track whether first column needs to be 0 or not.

        Rows = len(matrix)
        Cols = len(matrix[0])
        rowZero = False

        # determining which rows and columns needs to be 0.
        for row in range(0, Rows):
            for col in range(0, Cols):
                if matrix[row][col] == 0:

                    matrix[0][col] = 0
                    # here if row is not greater than one, then we set our flag to true.
                    if row > 0:
                         matrix[row][0] = 0
                    else:
                        rowZero = True
                    
        # goirng through each element excpet frist row and first column,and making them 0, if needed.
        for row in range(1, Rows):
            for col in range(1, Cols):
                if matrix[0][col] == 0  or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            # then i need to make first column 0.
            for R in range(0, Rows):
                matrix[R][0] = 0

        if rowZero == True:
            # then i need to make a first row zero
            for C in range(0, Cols):
                matrix[0][C] = 0
        
        return matrix
