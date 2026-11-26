class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n+1) for _ in range(n)] 

        def dp(i, j):
            if i == len(nums):
                return 0
            if memo[i][j+1] != -1:
                return memo[i][j+1]
            if j == -1 or nums[i] > nums[j]:
                # extend path and set j to prev chosen element
                memo[i][j+1] = max(1 + dp(i + 1, j=i), 0 + dp(i+1, j))
                # in take: see whether at each point taking or skipping is better
            else:
                # skip branch
                memo[i][j+1] = 0 + dp(i+1, j)
            return memo[i][j+1]

        return dp(0,-1)


        
                
