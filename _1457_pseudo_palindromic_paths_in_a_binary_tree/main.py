# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = [0 for _ in range(10)]
        result = 0

        def backtracking(root):
            nonlocal count
            nonlocal result

            count[root.val] += 1
            if not root.left and not root.right:
                nbOdd = 0
                for c in count:
                    if c % 2 == 1:
                        nbOdd += 1

                if nbOdd <= 1:
                    result += 1

                count[root.val] -= 1
                return

            
            if root.left:
                backtracking(root.left)

            if root.right:
                backtracking(root.right)

            count[root.val] -= 1

        backtracking(root)
        return result