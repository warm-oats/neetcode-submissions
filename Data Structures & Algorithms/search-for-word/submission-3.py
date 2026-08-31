class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False

        def backtrack(row: int, col: int, substr: str, word_index: int, prev_indexes: List[List[int]]) -> bool:
            if (row >= len(board)
            or row < 0
            or col >= len(board[row])
            or col < 0):
                return False

            if [row, col] in prev_indexes:
                return False

            curr_char = board[row][col]

            if curr_char != word[word_index]:
                return False

            substr += curr_char
            prev_indexes.append([row, col])

            if substr == word:
                return True

            check_1 = backtrack(row + 1, col, substr, word_index + 1, prev_indexes)
            check_2 = backtrack(row - 1, col, substr, word_index + 1, prev_indexes)
            check_3 = backtrack(row, col + 1, substr, word_index + 1, prev_indexes)
            check_4 = backtrack(row, col - 1, substr, word_index + 1, prev_indexes)

            substr = substr[:-1]
            prev_indexes.pop()

            return check_1 or check_2 or check_3 or check_4

        for row in range(len(board)):
            for col in range(len(board[row])):
                res = res or backtrack(row, col, '', 0, [])

        return res