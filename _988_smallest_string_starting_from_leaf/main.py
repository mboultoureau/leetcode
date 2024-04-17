# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        best = None

        def dfs(root, current):
            nonlocal best
            current = chr(root.val + ord('a'))  + current

            if not root.left and not root.right:
                if not best or current < best:
                    best = current
                return

            if root.left:
                dfs(root.left, current)
            
            if root.right:
                dfs(root.right, current)

        dfs(root, "")

        return best