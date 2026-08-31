class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        minutes = 0
        fresh_fruits = 0

        # Rotten fruit but cannot affect all fresh fruit

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    fresh_fruits += 1
                if grid[row][col] == 2:
                    queue.append([row, col])
                    visited.add((row, col))

        if not queue:
            return -1 if fresh_fruits > 0 else fresh_fruits

        def addFruit(row: int, col: int):
            if (row < 0) or (row >= len(grid)) or (col < 0) or (col >= len(grid[row])):
                return

            if grid[row][col] == 0 or (row, col) in visited:
                return

            queue.append([row, col])
            visited.add((row, col))

        fresh_fruits += len(queue)

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                fresh_fruits -= 1

                addFruit(row + 1, col)
                addFruit(row - 1, col)
                addFruit(row, col + 1)
                addFruit(row, col - 1)

            if queue:
                minutes += 1

        return minutes if fresh_fruits == 0 else -1