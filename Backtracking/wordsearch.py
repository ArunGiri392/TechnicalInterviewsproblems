class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS= len(board)
        COLS = len(board[0])
        path = set()

        def dfs(row, col, index):
            if index == len(word):
                return True

            if row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] != word[index] or (row,col) in path:
                return False
          
            path.add((row, col))


            result =  dfs(row + 1, col, index + 1) or dfs(row - 1, col, index + 1) or dfs(row, col + 1, index + 1) or dfs(row, col - 1, index + 1)
            path.remove((row, col))
            return result

        
        index = 0
        for row in range(0, ROWS):
            for col in range(0, COLS):
                    if dfs(row, col, index) == True:
                        return True
        return False


        # Time comlexity -- For each cell in grid, we are calling dfs. so that makes o(M * N) * DFS CALLS
        # o(M * N) * DFS CALLS  . AT EACH CALL, WE MAKE FOUR DFS CALL IN FOUR DIRECTIONS, AND WE STOP WHEN INDEX BECOMES LENGTH OF WORD. SO THAT MAKES 4^N WHEN N IS LENGTH OF WORD. 
        # SO OVERALL TIME COMPLEXITY -- o(M * N) * 4^N

        # Space Complexity:

# The space complexity is primarily due to the recursion stack and the visited set.
# The recursion depth can go up to the length of the input word k.
# The visited set can contain at most m*n distinct cell indices.
# Therefore, the space complexity is O(k + m*n).
