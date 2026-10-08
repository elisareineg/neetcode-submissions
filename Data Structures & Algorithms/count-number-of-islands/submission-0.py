
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        row = len(grid) - 1
        col = len(grid[0]) - 1
        numIslands = 0
        def dfs(r,c):
            if r < 0 or r > row  or c < 0 or c > col or grid[r][c] != '1':
                return 
            grid[r][c] = '0' # mark visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)  

        for r in range(row + 1):
            for c in range(col+ 1):
                if grid[r][c] == '1':
                    numIslands += 1
                    dfs(r,c)
        return numIslands
        
