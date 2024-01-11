# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def bfs(root: Optional[TreeNode], maximum: int, minimum: int) -> int:
            result = max(
                abs(maximum - root.val),
                abs(minimum - root.val),
            )

            maxValue = max(maximum, root.val)
            minValue = min(minimum, root.val)

            if root.left:
                result = max(result, bfs(root.left, maxValue, minValue))

            if root.right:
                result = max(result, bfs(root.right, maxValue, minValue))

            return result

        return bfs(root, root.val, root.val)