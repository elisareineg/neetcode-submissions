class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, path, remaining_target):
            if remaining_target == 0:
                res.append(path[:])
                return
            
            for i in range(idx, len(nums)):
                if nums[i] <= remaining_target: 
                    path.append(nums[i])
                    dfs(i, path, remaining_target - nums[i])
                    path.pop()   


        dfs(0, [], target)
        return res