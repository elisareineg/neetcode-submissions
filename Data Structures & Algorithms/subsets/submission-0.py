class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, path):
            if idx == len(nums): # reached end of nums
                res.append(path[:]) # append entire path to result
                return
            
            # include
            path.append(nums[idx])
            dfs(idx + 1, path)

            # exclude
            path.pop()
            dfs(idx + 1, path)


        i = 0
        dfs(i, [])

        return res