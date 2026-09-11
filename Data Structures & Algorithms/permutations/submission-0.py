class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in nums:
                if i not in path:
                    path.append(i)
                    dfs(path)
                    path.pop()

            
        dfs([])
        return res

            


            