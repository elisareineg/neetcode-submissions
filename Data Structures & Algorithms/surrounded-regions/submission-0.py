class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        zeros = set() # coordinates of border zeros
        zeroReach = set() # reachable

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                    zeros.add((r,c))

        # dfs into each 0 coordinate, add cells that are reachable and add to set

        def dfs(r,c,reach):
            if r < 0 or r >= m or c < 0 or c >= n or (r,c) in reach or board[r][c] == 'X':
                return
            reach.add((r,c))
            dfs(r-1, c, reach)
            dfs(r+1, c, reach)
            dfs(r, c - 1, reach)
            dfs(r, c + 1, reach)


        for cell in zeros:
            r, c = cell
            dfs(r,c, zeroReach)
            
        # traverse board, if there are zeros not in zeros or zeroReach, change them to an X
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r,c) not in zeros and (r,c) not in zeroReach:
                    board[r][c] = 'X'



