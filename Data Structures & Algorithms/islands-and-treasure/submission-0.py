from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        # add every treasure to the queue 
        for r in range(rows):
            for c in range(cols):
                # if this cell is a treasure, append (r, c)
                if grid[r][c] == 0:
                    queue.append((r,c))

        # one BFS loop that spreads from all treasures at once
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != INF:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))
