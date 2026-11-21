class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # 2d table, reuses answers for short substrings
        count = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    # j - i <= 2: handles short substrings 
                    # anything longer: checks table
                    dp[i][j] = True # palindrome
                    
        # get count of entries in table that are True
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j]:
                    count += 1

        return count
