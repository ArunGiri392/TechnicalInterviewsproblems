class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left = 0
        right = len(matrix) - 1
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1
        
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j],matrix[j][i]  = matrix[j][i], matrix[i][j]
        return matrix

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        

        for i in range(0,ROWS):
            for j in range(i + 1, ROWS):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        for row in matrix:
            left = 0
            right = len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
        return matrix

