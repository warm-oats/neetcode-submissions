class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_hashmap = defaultdict(list)
        sub_box_hashmap = defaultdict(list)

        for row_index, row in enumerate(board):
            starting_index = 0

            if (row_index <= 2):
                starting_index = 0
            elif (row_index >= 3 and row_index <= 5):
                starting_index = 3
            else:
                starting_index = 6

            row_hashset = set()

            for index, item in enumerate(row):
                #Create arrays for columns
                col_hashmap[index].append(item)

                #Check row duplicate
                if item not in row_hashset:
                    row_hashset.add(item)
                elif item != '.':
                    return False

                #Create array for sub-box
                hashmap_append_index = math.floor((index / len(row)) * 3 + starting_index)
                
                sub_box_hashmap[hashmap_append_index].append(item)

        for col in col_hashmap.values():
            col_hashset = set()

            for col_item in col:
                if col_item not in col_hashset:
                    col_hashset.add(col_item)
                elif col_item != '.':
                    return False
        
        for sub_box_arr in sub_box_hashmap.values():
            sub_box_hashset = set()

            for sub_box_item in sub_box_arr:
                if sub_box_item not in sub_box_hashset:
                    sub_box_hashset.add(sub_box_item)
                elif sub_box_item != '.':
                    return False
        
        return True


            

                

