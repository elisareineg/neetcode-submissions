class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, remaining_target, path):
            if remaining_target == 0:
                res.append(path[:])
                return

            for i in range(idx, len(candidates)):
                # skip duplicates at the same recursion level
                if i > idx and candidates[i] == candidates[i - 1]: # i > idx → later choices at the same level
                    continue

                if candidates[i] > remaining_target:
                    break  # pruning because array is sorted

                path.append(candidates[i])
                dfs(i + 1, remaining_target - candidates[i], path)
                path.pop()

        dfs(0, target, [])
        return res