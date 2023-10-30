class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for this problem, it is given that, the rows are already sorted, and the The first integer of each row is greater than the last integer of the previous row.

        # so the logic here is:
        # keep left at first index in 2d list, and right at last, 
        # calculate the mid, which is a list, because we are working with the 2d list.
        # so, in the mid, we take two elements: first of mid, and last of mid,
        # if target is less than first of mid, then, our target is defineatly on the left side of mid, so make right = mid - 1.
        # if target is greater than the last of mid, our target is definearly on the right side of the mid, so we make left = mid + 1

        # if neither of case is true, it means , the current target might be on the mid or might not be, so we have to have a binary search on the row to search. 

        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_first = matrix[mid][0]
            mid_last = matrix[mid][-1]

            if target < mid_first:
                # it means, target may lies on the left side of the mid
                right = mid - 1
            
            elif target > mid_last:
                 # it means, target may lies on the right side of the mid
                left = mid + 1
           
            else:
                 # it means, target may or may not lie on the current row (mid)
                 # so we do another binary search, on this row, to find it out.
                # we use mid, because mid represents our current row.
                left = 0
                right = len(matrix[0]) - 1
                while left <= right:
                    middle = (left + right) // 2
                    if target == matrix[mid][middle]:
                        return True
                    elif target < matrix[mid][middle]:
                        right = middle - 1
                    elif target > matrix[mid][middle]:
                        left = middle + 1
                return False
        
# Time complexity of this code is o(log(m*n))