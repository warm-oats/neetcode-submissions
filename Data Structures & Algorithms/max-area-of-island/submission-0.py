class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited_indices = set()

        def dfs(row: int, col: int) -> None:
            if (row < 0) or (row >= len(grid)) or (col < 0) or (col >= len(grid[row])):
                return

            if grid[row][col] == 0 or (row, col) in visited_indices:
                visited_indices.add((row, col))
                return

            visited_indices.add((row, col))

            nonlocal area
            area += 1

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row, col) not in visited_indices:
                    area = 0
                    dfs(row, col)
                    max_area = max(max_area, area)

        return max_area