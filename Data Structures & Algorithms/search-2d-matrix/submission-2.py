class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start = 0 
        row_end = len(matrix) - 1

        while row_end >= row_start:
            row_middle = math.floor((row_start + row_end) / 2)

            if target > matrix[row_middle][-1]:
                row_start = row_middle + 1
            elif target < matrix[row_middle][0]:
                row_end = row_middle - 1
            else:
                target_row = matrix[row_middle]
                col_start = 0
                col_end = len(target_row) - 1

                while col_end >= col_start:
                    col_middle = math.floor((col_start + col_end) / 2)

                    if target > target_row[col_middle]:
                        col_start = col_middle + 1
                    elif target < target_row[col_middle]:
                        col_end = col_middle - 1
                    else:
                        return True
                
                return False
        
        return False
