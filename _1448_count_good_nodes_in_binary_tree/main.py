# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visit(self, root: TreeNode, max: int) -> int:
        if not root:
            return 0

        count = 0

        if root.val >= max:
            count = 1
            max = root.val

        count += self.visit(root.left, max)
        count += self.visit(root.right, max)

        return count

    def goodNodes(self, root: TreeNode) -> int:
        return self.visit(root, -math.inf)