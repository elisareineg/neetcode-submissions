class Solution():
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)

        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float("inf")
            if memo[remaining] != -1:
                return memo[remaining]

            best = float("inf")
            for coin in coins:
                # try using this coin last, update best
                best = min(best, 1 + dp(remaining - coin))
            memo[remaining] = best
            return best

        result = dp(amount)
        return result if result != float("inf") else -1  # handle the case where amount can't be made