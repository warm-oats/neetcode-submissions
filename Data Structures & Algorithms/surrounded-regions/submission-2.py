class Solution:
    def solve(self, board: List[List[str]]) -> None:
        invalids = set()

        def bfs(row: int, col: int):
            if (row < 0) or (row >= len(board)) or (col < 0) or (col >= len(board[row])):
                return

            if board[row][col] == 'X' or (row, col) in invalids:
                return
            
            invalids.add((row, col))

            bfs(row + 1, col)
            bfs(row - 1, col)
            bfs(row, col - 1)
            bfs(row, col + 1)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if row == 0 or col == 0 or row == len(board) - 1 or col == len(board[row]) - 1:
                    if board[row][col] == 'O':
                        bfs(row, col)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'O' and (row, col) not in invalids:
                    board[row][col] = 'X'

        


            

        