class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)] # 2d table, reuses answers for short substrings

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    # j - i <= 2: handles short substrings 
                    # anything longer: checks table
                    dp[i][j] = True # palindrome
                    
                    if resLen < (j - i + 1):
                        resIdx = i # store index of longest length
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]



        """
        Two ptr
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i # center of string
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1] # inclusive of r
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1] # inclusive of r
                l -= 1
                r += 1
        return res
        """
       