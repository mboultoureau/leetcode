# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = {}
        maximum = 0

        def incrementMode(root: Optional[TreeNode]):
            nonlocal maximum

            if not root:
                return

            if root.val in counter:
                counter[root.val] += 1
                maximum = max(counter[root.val], maximum)
            else:
                counter[root.val] = 1
                maximum = max(1, maximum)

            incrementMode(root.left)
            incrementMode(root.right)

        incrementMode(root)
        result = []

        for key, value in counter.items():
            if value == maximum:
                result.append(key)

        return result

