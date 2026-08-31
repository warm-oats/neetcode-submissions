class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    visited.add((row, col))
        
        def addIsland(row: int, col: int):
            if (row < 0) or (row >= len(grid)) or (col < 0) or (col >= len(grid[row])):
                return

            if grid[row][col] == -1 or (row, col) in visited:
                return

            queue.append([row, col])
            visited.add((row, col))

        dist = 0

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                grid[row][col] = dist

                addIsland(row + 1, col)
                addIsland(row - 1, col)
                addIsland(row, col + 1)
                addIsland(row, col - 1)

            dist += 1