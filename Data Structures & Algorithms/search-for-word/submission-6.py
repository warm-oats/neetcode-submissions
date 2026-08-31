class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row: int, col: int, visited: List[List[int]], char_index: int):
            if ((row < 0) 
            or (col < 0) 
            or (row >= len(board)) 
            or (col >= len(board[row]))
            or [row, col] in visited
            or word[char_index] != board[row][col]):
                return False

            char_index += 1
            visited.append([row, col])

            if char_index == len(word):
                return True

            return (backtrack(row + 1, col, visited.copy(), char_index) 
            or backtrack(row - 1, col, visited.copy(), char_index) 
            or backtrack(row, col + 1, visited.copy(), char_index) 
            or backtrack(row, col - 1, visited.copy(), char_index))

        for row in range(len(board)):
            for col in range(len(board[row])):
                if backtrack(row, col, [], 0):
                    return True

        return False


            