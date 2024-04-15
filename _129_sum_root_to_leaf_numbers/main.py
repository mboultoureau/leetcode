# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, current):
            if not root:
                return 0

            current = current * 10 + root.val

            if not root.left and not root.right:
                return current
            
            return dfs(root.left, current) + dfs(root.right, current)


        return dfs(root, 0)

