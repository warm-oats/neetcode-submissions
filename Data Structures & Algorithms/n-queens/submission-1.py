class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = ['.' * n] * n

        def backtrack(curr_board: List[str], row: int):
            # Check row out of bound, if so valid board
            if row == len(curr_board):
                res.append(curr_board.copy())
                return

            for col in range(n):
                curr_board[row] = curr_board[row][:col] + 'Q' + curr_board[row][col+1:]

                # Check row, col, diagonal of current queen value
                if valid_Q_pos(curr_board, row, col):
                    backtrack(curr_board, row + 1)
                
                curr_board[row] = curr_board[row][:col] + '.' + curr_board[row][col+1:]

        def valid_Q_pos(curr_board: List[str], row_i: int, col_i: int) -> bool:
            # Check col validity
            for row in range(len(curr_board)):
                if row != row_i and curr_board[row][col_i] == 'Q':
                    return False

            # Check row validity
            for col in range(len(curr_board[row_i])):
                if col != col_i and curr_board[row_i][col] == 'Q':
                    return False

            # Check top to bottom diagonal validity
            min_row, min_col = row_i - min(row_i, col_i), col_i - min(row_i, col_i)

            while max(min_row, min_col) < n:
                if min_row != row_i and min_col != col_i and curr_board[min_row][min_col] == 'Q':
                    return False

                min_row += 1
                min_col += 1

            # Check bottom to top diagonal validity
            diff_factor = min(abs(0 - col_i), (n - 1) - row_i)
            max_row, min_col = row_i + diff_factor, col_i - diff_factor

            while max_row > -1 and min_col < n:
                if [max_row, min_col] != [row_i, col_i] and curr_board[max_row][min_col] == 'Q':
                    return False

                max_row -= 1
                min_col += 1

            # (1, 1), diff = 1, max_row = (2,0)

            # (0,2) 

            return True

        backtrack(board, 0)

        return res
        