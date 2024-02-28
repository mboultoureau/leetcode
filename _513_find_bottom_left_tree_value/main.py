# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        maxDepth = 0
        maxLeft = 0
        

        def explore(root, depth):
            nonlocal maxDepth
            nonlocal maxLeft

            if not root:
                return

            depth += 1

            if depth > maxDepth:
                maxDepth = depth
                maxLeft = root.val

            explore(root.left, depth)
            explore(root.right, depth)
        
        explore(root, 0)

        return maxLeft 