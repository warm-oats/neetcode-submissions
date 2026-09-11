class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left = 0
        row_right = len(matrix) - 1

        while row_left <= row_right:
            mid = (row_left + row_right) // 2
            cur_row = matrix[mid]
            left = 0
            right = len(cur_row) - 1

            if target >= cur_row[left] and target <= cur_row[right]:
                while left <= right:
                    mid = (left + right) // 2

                    if cur_row[mid] == target:
                        return True
                    
                    if cur_row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                return False
            
            if target < cur_row[left]:
                row_right = mid - 1
            else:
                row_left = mid + 1
        
        return False
        
        

        