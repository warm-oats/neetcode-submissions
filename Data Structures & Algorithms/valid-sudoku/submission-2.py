class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = [[] for _ in range(len(board))]
        col_hash = [[] for _ in range(len(board[0]))]
        box_hash = [[] for _ in range(len(board)*len(board[0])//9)]

        for row_i in range(len(board)):
            for col_i in range(len(board[row_i])):
                board_num = board[row_i][col_i]
                box_index = (row_i//3)*3+(col_i//3)

                if board_num == '.':
                    continue

                if board_num in row_hash[row_i] or board_num in col_hash[col_i]:
                    return False
                
                if board_num in box_hash[box_index]:
                    return False

                row_hash[row_i].append(board_num)
                col_hash[col_i].append(board_num)
                box_hash[box_index].append(board_num)

        return True