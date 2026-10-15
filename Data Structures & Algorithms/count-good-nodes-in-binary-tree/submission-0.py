# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        # check at each root node, if it's left or right child is greater in value
        # if not, increment count
        # if we reach a leaf node, check if greater than maxNode
        value = 0
        def dfs(node, maxNode):
            nonlocal value
            if not node:
                return value
            val = node.val
            if val >= maxNode:
                value += 1
            maxNode = max(val, maxNode)
            return dfs(node.left, maxNode) + dfs(node.right, maxNode)
        dfs(root, -101)
        return value

        
        