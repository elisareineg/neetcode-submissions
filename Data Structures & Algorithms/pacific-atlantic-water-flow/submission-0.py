
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        pReach = set()
        aReach = set()
        res = []

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    pacific.add((r,c))
                if r == m - 1 or c == n - 1:
                    atlantic.add((r,c))

        
        def dfs(r,c, reachSet, prevHeight): # start from border cells
            if r < 0 or r >= m or c < 0 or c >= n or (r,c) in reachSet or heights[r][c] < prevHeight:
                return
            reachSet.add((r,c)) # will be pReach or aReach
            # dfs into heights greater than or equal to current cells height
            dfs(r-1, c, reachSet, heights[r][c])
            dfs(r+1, c, reachSet, heights[r][c])
            dfs(r, c-1, reachSet, heights[r][c])
            dfs(r, c + 1, reachSet, heights[r][c])

        for cell in atlantic:
            r,c = cell
            dfs(r,c, aReach, heights[r][c])

        for cell in pacific:
            r,c = cell
            dfs(r,c, pReach, heights[r][c])

        for cell in pReach:
            r,c = cell
            if (r,c) in aReach:
                res.append((r,c)) # in both sets


        return res
            
            
