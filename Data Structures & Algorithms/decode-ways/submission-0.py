class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)
        def dp(i): # everytime we see a 0, check if it's leading
            # check dp(i) and dp(i+1)
            if i < 0:
                return 1
            if memo[i] != -1:
                return memo[i]
            total = 0 # every total is diff
            if (i - 1 >= 0 and 10 <= int(s[i-1:i+1]) <= 26):
                total += dp(i-2)
            if s[i] != "0":
                total += dp(i-1)
            memo[i] = total
            return total

        return dp(len(s) - 1)