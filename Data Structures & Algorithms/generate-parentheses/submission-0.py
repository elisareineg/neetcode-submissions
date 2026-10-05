class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(opens, closes):
            # ( less than n 
            # ) less than opens
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if opens < n:
                path.append("(")
                dfs(opens + 1, closes)
                path.pop()
            if closes < opens:
                path.append(")")
                dfs(opens, closes + 1)
                path.pop()
        dfs(0,0)
        return res
            

            