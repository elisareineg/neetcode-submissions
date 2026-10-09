class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        row = len(grid) - 1
        col = len(grid[0]) - 1

        def dfs(r, c,):
            if r < 0 or r > row or c < 0 or c > col or grid[r][c] == 0:
                return 0
            grid[r][c] = 0 # mark visited
            return 1 + dfs(r - 1, c) + dfs(r + 1 ,c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(row + 1):
            for c in range(col + 1):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    maxArea = max(maxArea, area)

        return maxArea