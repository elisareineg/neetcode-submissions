from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for pair in edges: 
            a, b = pair
            adj[a].append(b) 
            adj[b].append(a)

        visited = set() # don't clear nodes
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nbr in adj[node]:
                # new component: node is none
                dfs(nbr)
        count = 0
        for i in range(n):
            # if i already visited: connected
            # if i not visited: new component
            if i not in visited:
                count += 1
            dfs(i)

        return count
            
            

        