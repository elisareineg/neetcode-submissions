class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(idx):
            if idx == len(nums):
                res.append(subset[:])
                return
            # include nums[idx]
            subset.append(nums[idx])
            dfs(idx + 1)
            subset.pop()

            # exclude: branch past all copies of curr val to avoid duplicate subsets
            curVal = nums[idx]
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx+1)

        dfs(0)
        return res

            
            
            
            