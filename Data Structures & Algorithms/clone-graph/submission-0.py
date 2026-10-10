"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj = {} # original node -> copy
 
        if not node:
            return None

        def dfs(node):
            if node in adj:
                return adj[node]
            newNode = Node(node.val, None)
            adj[node] = newNode
            for nbr in node.neighbors:
                copy = dfs(nbr)
                newNode.neighbors.append(copy)
            return newNode
            
        return dfs(node)