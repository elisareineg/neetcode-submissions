from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # store a -> b and inverse (b -> a) with associated value

        adj = defaultdict(list)
        for i, pair in enumerate(equations):
            a, b = pair
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def dfs(node, visited, total, target): # total will store the calculated values
            if node == target:
                return total
            visited.add(node)
            for nbr, wt in adj[node]:
                if nbr in visited: 
                    continue
                result = dfs(nbr, visited, total * wt, target)
                if result != -1.0:
                    return result
            return -1.0
            

        res = []
        for q in queries:
            a, b = q
            if a not in adj or b not in adj:
                res.append(-1.0)
                continue
            else:
                total = dfs(a, set(), 1, b)
                res.append(total)
        return res
            