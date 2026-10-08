class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            target = -nums[i]
            while j < k:
                total = nums[j] + nums[k]
                if total == target:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    k -= 1
        return res