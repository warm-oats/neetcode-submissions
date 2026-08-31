class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def backtrack(row: int, col: int, char_index: int):
            if ((row < 0) 
            or (col < 0) 
            or (row >= len(board)) 
            or (col >= len(board[row]))
            or (row, col) in visited
            or word[char_index] != board[row][col]):
                return False

            char_index += 1
            visited.add((row, col))

            if char_index == len(word):
                return True

            if (backtrack(row + 1, col, char_index) 
            or backtrack(row - 1, col, char_index) 
            or backtrack(row, col + 1, char_index) 
            or backtrack(row, col - 1, char_index)):
                visited.remove((row, col))
                return True
            else:
                visited.remove((row, col))
                return False

        for row in range(len(board)):
            for col in range(len(board[row])):
                if backtrack(row, col, 0):
                    return True

        return False


            