class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #    l              R
    #   T 1   2   3    4
    #    5   6   7    8
    #    9   10  11   12
    #    B

        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        result = []
        while left < right and top < bottom:
            # here firstly, i want to go from left to right direction.
            for i in range(left, right):
                result.append(matrix[top][i])
            # after this we have completed the printing of the first row, so we can decrease the top pointer, which was pointing to the first row.
            top += 1


            # now, we have to go from right most top to bottom.
            # because, above top has already been increased by 1, so, here we do not face problem of prinitng same element.  ie we do not want to print 4 double times, as it has already been printied when coming from left to right, so because top has increased by 1, and doing range top to bottom, eliminates this problem.
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if left >= right or top >= bottom:
                break

            # now go from right to left, here also because right has been shifted by 1, we do not print same element.
            # because we are doing reverse order, add -1, at last and also left - 1, ie what happens in reverse.
            for i in range(right - 1, left-1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # now go from bottom to top.
            for i in range(bottom - 1, top -1, -1):
                result.append(matrix[i][left])
            left += 1
        return result





