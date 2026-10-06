class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        visited = set()
        def dfs(row, col, idx): # idx of given word
            if row >= m or row < 0 or col >= n or col < 0 or board[row][col] != word[idx] or (row, col) in visited:
                return False
            visited.add((row, col))
            if idx == len(word) - 1:
                return True
            if (dfs(row - 1, col, idx + 1) or dfs(row + 1, col, idx + 1) or dfs(row, col + 1, idx + 1) or dfs(row, col - 1, idx + 1)):
                visited.remove((row,col))
                return True
            else:
                visited.remove((row,col))
                return False
            

        for r in range(m):
            for c in range(n):
                if dfs(r,c, 0):
                    return True
        return False
            
        

            
            
