class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_visited, atlantic_visited = set(), set()
        pac_queue, atl_queue = deque(), deque()
        atl_res, pac_res = set(), set()

        for row in range(len(heights)):
            for col in range(len(heights[row])):
                if row == 0 or col == 0:
                    pacific_visited.add((row, col))
                    pac_queue.append([row, col])
                if row == len(heights) - 1 or col == len(heights[row]) - 1:
                    atlantic_visited.add((row, col))
                    atl_queue.append([row, col])

        def add_cell(par_cell: List[int], cell: List[int], ocean: str):
            par_row = par_cell[0]
            par_col = par_cell[1]
            cell_row = cell[0]
            cell_col = cell[1]

            if (cell_row < 0) or (cell_row >= len(heights)) or (cell_col < 0) or (cell_col >= len(heights[cell_row])):
                return

            if heights[par_row][par_col] > heights[cell_row][cell_col]:
                return 

            if ocean == 'pacific' and (cell_row, cell_col) not in pacific_visited:
                pacific_visited.add((cell_row, cell_col))
                pac_queue.append([cell_row, cell_col])
            
            if ocean == 'atlantic' and (cell_row, cell_col) not in atlantic_visited:
                atlantic_visited.add((cell_row, cell_col))
                atl_queue.append([cell_row, cell_col])

        while pac_queue or atl_queue:
            for i in range(len(pac_queue)):
                par_row, par_col = pac_queue.popleft()

                pac_res.add((par_row, par_col))

                add_cell([par_row, par_col], [par_row + 1, par_col], 'pacific')
                add_cell([par_row, par_col], [par_row - 1, par_col], 'pacific')
                add_cell([par_row, par_col], [par_row, par_col + 1], 'pacific')
                add_cell([par_row, par_col], [par_row, par_col - 1], 'pacific')

            for i in range(len(atl_queue)):
                par_row, par_col = atl_queue.popleft()

                atl_res.add((par_row, par_col))

                add_cell([par_row, par_col], [par_row + 1, par_col], 'atlantic')
                add_cell([par_row, par_col], [par_row - 1, par_col], 'atlantic')
                add_cell([par_row, par_col], [par_row, par_col + 1], 'atlantic')
                add_cell([par_row, par_col], [par_row, par_col - 1], 'atlantic')

        res = []

        for row in range(len(heights)):
            for col in range(len(heights[row])):
                if (row, col) in atl_res and (row, col) in pac_res:
                    res.append([row, col])

        return res




            

            