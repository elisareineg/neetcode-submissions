class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [-1] * len(s) # track indexes at which there is a word in the dict at suffix of i (store True or False at memo[i])

        def dp(i):
            if i == len(s):
                return True
            if memo[i] != -1:
                return memo[i]
            
            j = i + 1
            for j in range(len(s)):
                if s[i:j+1] in wordDict and dp(j+1): # see if whether rest of string after this word can be split
                    memo[i] = True
                    return memo[i]
                
            memo[i] = False
            return memo[i]


        return dp(0)


        

            