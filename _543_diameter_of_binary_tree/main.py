# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Solution 2 : With NeetCode
        result = 0

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal result

            if root == None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            result = max(result, left + right)

            return 1 + max(left, right)

        dfs(root)
        return result

    # Solution 1 : good memory
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     return self.dfs(root)[0]

    # def dfs(self, root: Optional[TreeNode]) -> int:
    #     if root == None:
    #         return [0, 0]

    #     left, right = self.dfs(root.left), self.dfs(root.right)
    #     maximum = max(left[1] + right[1], left[0], right[0])

    #     return [maximum, 1 + max(left[1], right[1])]