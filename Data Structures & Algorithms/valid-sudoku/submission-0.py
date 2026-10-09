class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # box = board[]
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if (board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in box[(r//3, c//3)]) and board[r][c] != ".":
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                box[(r//3, c//3)].add(board[r][c])

        return True