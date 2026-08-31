class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited_indices = set()

        def dfs(row: int, col: int) -> None:
            if (row < 0) or (row >= len(grid)) or (col < 0) or (col >= len(grid[row])):
                return 0

            if grid[row][col] == 0 or (row, col) in visited_indices:
                visited_indices.add((row, col))
                return 0

            visited_indices.add((row, col))

            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                max_area = max(max_area, dfs(row, col))

        return max_area