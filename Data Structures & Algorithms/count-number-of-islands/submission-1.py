
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        row = len(grid) - 1
        col = len(grid[0]) - 1
        numIslands = 0
        def dfs(r,c):
            if r > row or r < 0 or c > col or c < 0 or grid[r][c] != "1":
                return False

            grid[r][c] = "0" # mark visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return True

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(r, c):
                    numIslands += 1
        return numIslands
        
