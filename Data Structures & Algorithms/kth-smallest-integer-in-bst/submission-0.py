# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        replacements = 0
        result = None

        def dfs(node):
            nonlocal replacements, result
            if not node:
                return
            dfs(node.left)
            replacements += 1
            if replacements == k:
                result = node.val
                return
            dfs(node.right)

        dfs(root)
        return result

            