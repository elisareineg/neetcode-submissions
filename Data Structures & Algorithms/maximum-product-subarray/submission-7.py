class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            best = max(best, curMax)
        return best