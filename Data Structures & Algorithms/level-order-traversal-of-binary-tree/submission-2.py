# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        output = deque([root]) # initialize w/ root

        while output:
            levelSize = len(output) # num nodes at curr level
            currLevel = []

            for _ in range(levelSize):
                node = output.popleft()
                currLevel.append(node.val)
                if node.left:
                    output.append(node.left)
                if node.right:
                    output.append(node.right)

            res.append(currLevel)

        return res

        

        
















    """
    # LeetCode 102: Binary Tree Level Order Traversal
# Return the node values level by level, left to right,
# as a list of lists: [[level 0], [level 1], ...]
#
# ---------------------------------------------------------------
# HINTS (read one at a time before looking at the solution)
# ---------------------------------------------------------------
#
# Hint 1:
#   "Level by level" is breadth-first search (BFS), not DFS.
#   BFS naturally visits all nodes at depth d before depth d + 1.
#
# Hint 2:
#   BFS uses a queue (first in, first out). In Python, use
#   collections.deque: append() to add on the right, popleft()
#   to remove from the left in O(1). A plain list's pop(0) is O(n).
#
# Hint 3:
#   The tricky part is knowing where one level ends and the next
#   begins. At the start of each level, the queue contains exactly
#   the nodes of that level. How can you use that?
#
# Hint 4:
#   Record len(queue) BEFORE processing a level, then pop exactly
#   that many nodes. Any children you append during that loop
#   belong to the next level and won't be popped yet.
#
# Hint 5:
#   Edge case: an empty tree (root is None) should return [].
#
# Hint 6:
#   Complexity target: O(n) time, O(w) space where w is the
#   maximum width of the tree (up to about n/2 for a full tree).
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
# SOLUTION 1: BFS with a queue
# ---------------------------------------------------------------

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Empty tree: no levels.
        if root is None:
            return []

        res = []
        q = deque([root])          # start with level 0

        while q:
            # Everything in the queue right now is exactly one level.
            # Freeze that count before we start adding children.
            level_size = len(q)
            level = []

            for _ in range(level_size):
                node = q.popleft()      # take from the front
                level.append(node.val)

                # Children go to the back of the queue. They belong
                # to the NEXT level, and level_size stops us from
                # processing them in this loop.
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res


# ---------------------------------------------------------------
# SOLUTION 2: DFS with depth tracking (alternative)
# ---------------------------------------------------------------
# Same output using recursion. Pass the depth down; the depth
# tells you which inner list a value belongs in. Visiting left
# before right keeps each level in left-to-right order.

class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if node is None:
                return
            # First time reaching this depth: open a new level list.
            if depth == len(res):
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res


# ---------------------------------------------------------------
# QUICK TRACE (Solution 1)
# ---------------------------------------------------------------
#
#         3
#        / \
#       9   20
#          /  \
#         15   7
#
# queue = [3]
#   level_size = 1: pop 3, push 9, 20       -> level [3]
# queue = [9, 20]
#   level_size = 2: pop 9 (no children),
#                   pop 20, push 15, 7      -> level [9, 20]
# queue = [15, 7]
#   level_size = 2: pop 15, pop 7           -> level [15, 7]
# queue = []  -> stop
#
# Result: [[3], [9, 20], [15, 7]]
#
# ---------------------------------------------------------------
# RELATED PROBLEMS (same template, small change)
# ---------------------------------------------------------------
# - Right Side View (199): take the LAST value of each level.
# - Zigzag Level Order (103): reverse every other level.
# - Max Depth (104): count how many levels there are.
    """