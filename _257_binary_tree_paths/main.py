# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []

        def explore(root, string):
            nonlocal result
            string += str(root.val)
            if not root.left and not root.right:
                result.append(string)

            if root.left:
                explore(root.left, string + "->")

            if root.right:
                explore(root.right, string + "->")


        explore(root, "")
        return result