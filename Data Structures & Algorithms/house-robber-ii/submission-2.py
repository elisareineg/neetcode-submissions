class Solution:
    def rob(self, nums: List[int]) -> int:
        memo0 = [-1] * len(nums)
        memoLen = [-1] * len(nums)

        def dp(start, end, memo): # top down
            if len(memo) <= 1:
                return nums[end]
            if end < start:
                return 0
            if memo[end] != -1:
                return memo[end]
            memo[end] = max(dp(start, end-2, memo) + nums[end], dp(start, end-1, memo))
            return memo[end]
        
        return max(dp(1, len(nums) - 1, memo0), dp(0, len(nums) - 2, memoLen))