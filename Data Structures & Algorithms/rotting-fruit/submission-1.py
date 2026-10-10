from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # use bfs, for every bfs call we will change every adjacent,horizontal fruit to a 2 if it's next to a rotten one, then increment a count until all fruits are rotten
        queue = deque()
        for r in range(m):
            for c in range(n):
                # find all the 2's and add to queue
                if grid[r][c] == 2:
                    queue.append((r,c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0 # increment each level 
        while queue:
            rotted = False
            
            for _ in range(len(queue)): # processes exactly one minute’s worth of oranges per round
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    rotted = True
                    queue.append((nr, nc))
            if rotted:
                count += 1
            

        # check if any 1's remain
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
                
        return count
        



