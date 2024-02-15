class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # going through each row.
     
        for row in board:
            hash_set = set()
            for number in row:
                if number == ".":
                    continue
                elif int(number) < 1 or int(number) > 9 or int(number) in hash_set:
                    return False
                hash_set.add(int(number))
        

        # going thrugh each column
        for col in range(0, 9):
            hash_set = set()
            for row in range(0, 9):
                number  = board[row][col]

                if number != ".":
                    number = int(board[row][col])
                
                if number == ".":
                    continue
                elif number < 1 or number > 9 or number in hash_set:
                    return False
                hash_set.add(number)
        
        # checking through all boxes.
        if self.sub_boxes(board, 0,0) and self.sub_boxes(board, 0,3) and self.sub_boxes(board,0,6) and self.sub_boxes(board, 3,0) and self.sub_boxes(board, 3,3) and self.sub_boxes(board, 3,6) and self.sub_boxes(board, 6,0) and self.sub_boxes(board, 6,3) and self.sub_boxes(board, 6,6) == True:
           return True
        return False

        




    # helper box function
    def sub_boxes(self, board, row , col):
        hash_set = set()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                number = board[i][j]

                if number != ".":
                    number = int(board[i][j])

                if number == ".":
                    continue
                elif number < 1 or number > 9 or number in hash_set:
                    return False
                hash_set.add(number)
        return True
