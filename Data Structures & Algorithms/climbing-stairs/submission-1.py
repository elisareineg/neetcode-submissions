class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)

        def dp(i):
            if memo[i] != 0:
                return memo[i]
            if i <= 2:
                memo[i] = i
                return memo[i]
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        return dp(n)
