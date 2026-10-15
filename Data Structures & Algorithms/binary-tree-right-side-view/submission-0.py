# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        # bfs: traverse each level through number of nodes at that level
        # if there's a left and right node, add both to the queue, but only right to the output array
        # if only left, add to queue and output

        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()
                if i == levelSize - 1 and i >= 0:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res