class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        dfs([])
        ├── dfs([1])
        │    ├── dfs([1,2])
        │    │    └── dfs([1,2,3])
        │    └── dfs([1,3])   
        ├── dfs([2])
        └── dfs([3])
        """


        res = []

        def dfs(path):
            if len(path) == len(nums): # ordering complete
                res.append(path[:]) # append copy
                return

            for i in nums: # try ever possible number that hasn't been used
                if i not in path: 
                    path.append(i)
                    dfs(path)
                    # level 1: 1 number, level 2: 2 numbers, level 3: 3 numbers
                    # ex: [1] -> [1,2] or [1,3] -> [1,2,3] or [1,3,2]
                    path.pop()

            
        dfs([])
        return res

            


            