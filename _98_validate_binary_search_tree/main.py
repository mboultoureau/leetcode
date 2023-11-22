# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.exploreSubtree(root, -math.inf, math.inf)

    def exploreSubtree(self, root: Optional[TreeNode], minimum, maximum) -> bool:
        if not root:
            return True

        if root.val <= minimum or root.val >= maximum:
            return False

        return self.exploreSubtree(root.left, minimum, root.val) and self.exploreSubtree(root.right, root.val, maximum)