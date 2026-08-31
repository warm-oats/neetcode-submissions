class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_hashmap = defaultdict(list)
        sub_box_hashmap = defaultdict(list)

        for row_index,row in enumerate(board):
            row_dup_set = set()

            for col_index,col_item in enumerate(row):
                col_sub_index = math.floor(col_index * 3 / 9)
                row_sub_index = math.floor(row_index * 3 / 9) * 3
                sub_box_index = col_sub_index + row_sub_index

                sub_box_hashmap[sub_box_index].append(col_item)

                # Add items to col hashmap
                col_hashmap[col_index].append(col_item)

                # Validate row
                if col_item in row_dup_set and col_item != '.':
                    return False
                else:
                    row_dup_set.add(col_item)
        
        # Validate column
        for col in col_hashmap.values():
            col_dup_set = set()

            for col_item in col:
                if col_item in col_dup_set and col_item != '.':
                    return False
                else:
                    col_dup_set.add(col_item)

        # Validate sub_box
        for sub_box in sub_box_hashmap.values():
            sub_box_dup_set = set()

            for item in sub_box:
                if item in sub_box_dup_set and item != '.':
                    return False
                else:
                    sub_box_dup_set.add(item)

        return True

        
                
