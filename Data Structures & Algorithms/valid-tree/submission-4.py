from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if len(edges) != n - 1:
                return False # more than 1 node
            return True # 1 node

        adj = defaultdict(list) # node -> nbrs
  
        for pair in edges:
            node, nbr = pair
            adj[node].append(nbr)
            adj[nbr].append(node) # inverse: undirected graph

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nbr in adj[node]:
                if nbr == parent:
                    continue
                if not dfs(nbr, node):
                    return False
            
            return True
    
        if dfs(0, -1) and len(visited) == n:
            return True
        return False


















    """
    # LeetCode 261: Graph Valid Tree
# Given n nodes labelled 0..n-1 and a list of undirected edges,
# return True if the edges form a valid tree.
#
# ---------------------------------------------------------------
# HINTS (read one at a time before looking at the solution)
# ---------------------------------------------------------------
#
# Hint 1:
#   What makes a graph a tree? Two conditions:
#     - no cycles
#     - connected (every node reachable from every other)
#
# Hint 2:
#   A tree with n nodes always has exactly n - 1 edges.
#   If len(edges) != n - 1, you can return False immediately.
#   With exactly n - 1 edges, "connected" and "no cycles" imply
#   each other, so checking connectivity alone is enough.
#
# Hint 3:
#   The edges are undirected, so store each edge in BOTH
#   directions in your adjacency list.
#
# Hint 4:
#   If you detect cycles with DFS directly, be careful: in an
#   undirected graph, the node you just came from (the parent)
#   is always a neighbour. Skip it, or every edge looks like a
#   cycle. (Hint 2 lets you avoid this entirely.)
#
# Hint 5:
#   Connectivity check: DFS from node 0, then compare the number
#   of visited nodes to n.
#
# Hint 6:
#   Complexity target: O(n + e) time and space.
#
#
#
#
#
#
#
#
#
#
# ---------------------------------------------------------------
# SOLUTION 1: edge count + DFS connectivity
# ---------------------------------------------------------------

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree on n nodes has exactly n - 1 edges.
        # Fewer: can't be connected. More: must contain a cycle.
        if len(edges) != n - 1:
            return False

        # Build an undirected adjacency list: add both directions.
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # DFS from node 0, marking every reachable node.
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)

        dfs(0)

        # With n - 1 edges, being connected guarantees no cycle,
        # so the graph is a tree iff DFS reached every node.
        return len(visited) == n


# ---------------------------------------------------------------
# SOLUTION 2: DFS with explicit cycle detection (no edge-count trick)
# ---------------------------------------------------------------
# Useful to know in case an interviewer asks you to detect the
# cycle directly.

class Solution2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node, parent):
            # Reaching an already-visited node means a cycle.
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                # Skip the edge we just came along. In an undirected
                # graph, the parent is always a neighbour.
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        # No cycle AND every node reached -> tree.
        # parent = -1 because node 0 has no parent.
        return dfs(0, -1) and len(visited) == n


# ---------------------------------------------------------------
# QUICK TRACES
# ---------------------------------------------------------------
#
# n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
#   4 edges == n - 1   -> continue
#   DFS from 0 visits {0,1,2,3,4} -> 5 == n -> True
#
#        0
#      / | \
#     1  2  3
#     |
#     4
#
# n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
#   5 edges != n - 1 (4) -> False  (1-2-3-1 is a cycle)
#
# n = 4, edges = [[0,1],[2,3]]
#   2 edges != n - 1 (3) -> False  (two separate pieces)
#
# n = 4, edges = [[0,1],[1,2],[2,0]]
#   3 edges == n - 1, but DFS from 0 visits {0,1,2} -> 3 != 4
#   -> False  (cycle 0-1-2, and node 3 is isolated)
    """