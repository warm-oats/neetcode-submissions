class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_index_row = 0
        end_index_row = len(matrix) - 1
        target_row = None

        while (start_index_row <= end_index_row):
            middle_index_row = math.floor((end_index_row + start_index_row) / 2)

            if target > matrix[middle_index_row][-1]:
                start_index_row = middle_index_row + 1
            elif target < matrix[middle_index_row][0]:
                end_index_row = middle_index_row - 1
            else:
                target_row = matrix[middle_index_row]
                break

        if not target_row:
            return False

        start_index = 0
        end_index = len(target_row) - 1

        while (start_index <= end_index):
            middle_index = math.floor((end_index + start_index) / 2)

            if target == target_row[middle_index]:
                return True
            elif target > target_row[middle_index]:
                start_index = middle_index + 1
            else:
                end_index = middle_index - 1

        return False

