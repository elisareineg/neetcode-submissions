class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def dp(i):
            if memo[i] != -1:
                return memo[i]
            if i <= 1:
                memo[i] = cost[i]
                return memo[i]
            memo[i] = min(dp(i-1), dp(i-2)) + cost[i]
            return memo[i]

        return min(dp(len(cost) - 1), dp(len(cost) - 2))