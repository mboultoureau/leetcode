# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = -math.inf

        def explore(root):
            nonlocal best

            if not root:
                return 0

            leftValue = explore(root.left)
            rightValue = explore(root.right)

            newBest = max(
                root.val,
                leftValue + root.val,
                rightValue + root.val
            )

            best = max(best, newBest, leftValue  + root.val + rightValue)

            return newBest

        explore(root)

        return best