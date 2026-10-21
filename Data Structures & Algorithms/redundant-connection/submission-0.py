class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]: 
                ra, rb = rb, ra
            parent[rb] = ra # attach smaller tree under larger 
            size[ra] += size[rb]
            return True

        for a, b in edges:
            if not union(a,b): # fail to connect edge / redundant
                return [a,b]


        
