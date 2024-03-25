# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        path = defaultdict(int)
        path[0] = 1

        def dfs(root, current):
            nonlocal path
            nonlocal count

            if not root:
                return

            current += root.val
            count += path[current - targetSum]
            path[current] += 1

            dfs(root.left, current)
            dfs(root.right, current)

            path[current] -= 1

        dfs(root, 0)

        return count