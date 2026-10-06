class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # TOP DOWN
        n = numRows
        memo = [-1] * n

        def dp(i):
            row = [-1] * (i + 1)
            if memo[i] != -1:
                return memo[i]
            if i == 0:
                memo[i] = [1]
                return memo[i]
            s = dp(i-1)
            for j in range(i + 1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] = s[j] + s[j -1]
            memo[i] = row
            return memo[i]

        dp(n-1)
        return memo
