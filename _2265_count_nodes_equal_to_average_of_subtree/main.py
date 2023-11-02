# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        def subtree(root: Optional[TreeNode]):
            nonlocal total

            if not root:
                return [0, 0]

            if not root.left and not root.right:
                total += 1
                return [1, root.val]

            [nbLeft, sumLeft] = subtree(root.left)
            [nbRight, sumRight] = subtree(root.right)

            [nbCurrent, sumCurrent] = [nbLeft + nbRight + 1, sumLeft + sumRight + root.val]
            if sumCurrent // nbCurrent == root.val:
                total += 1
            return [nbCurrent, sumCurrent]

        subtree(root)
        return total
