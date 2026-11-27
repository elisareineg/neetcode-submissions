class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums) 
        if (target % 2) != 0:
            return False
        target = target // 2
        memo = [[None] * (target + 1) for _ in range(n)]
        def dp(i, curSum):
            if curSum == target:
                return True
            if i >= n:
                return False
            if memo[i][curSum] is not None:
                return memo[i][curSum]

            # store T or F in memo
            # find a matching sum, return True immediately
            
            # include
            if curSum + nums[i] <= target:
                memo[i][curSum] = dp(i+1, curSum + nums[i]) or dp(i+1, curSum)

            # exclude
            else:
                memo[i][curSum] = dp(i+1, curSum)

            return memo[i][curSum]

        return dp(0, 0)