class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        if n == 2 or n == 3:
            return res

        def backtrack(row: int, chess_board: List[str]):
            nonlocal res

            if row >= n:
                res.append(chess_board.copy())
                return
            
            for col in range(n): 
                chess_board[row] = chess_board[row][:col] + 'Q' + chess_board[row][col+1:]

                if not has_collision(col, row, chess_board):
                    backtrack(row + 1, chess_board)

                chess_board[row] = chess_board[row][:col] + '.' + chess_board[row][col+1:]

        def has_collision(col: int, row: int, chess_board: List[str]) -> bool:
            # Check row collision
            for i in range(n):
                if chess_board[row][i] == 'Q' and i != col:
                    return True

            # Check col collision
            for i in range(n):
                if chess_board[i][col] == 'Q' and i != row:
                    return True

            # Check top to bottom diagonal validity
            min_row, min_col = row - min(row, col), col - min(row, col)

            while max(min_row, min_col) < n:
                if min_row != row and min_col != col and chess_board[min_row][min_col] == 'Q':
                    return True

                min_row += 1
                min_col += 1

            # Check bottom to top diagonal validity
            diff_factor = min(abs(0 - col), (n - 1) - row)
            max_row, min_col = row + diff_factor, col - diff_factor

            while max_row > -1 and min_col < n:
                if [max_row, min_col] != [row, col] and chess_board[max_row][min_col] == 'Q':
                    return True

                max_row -= 1
                min_col += 1

            return False
            
        backtrack(0, ['.' * n] * n)

        return res
