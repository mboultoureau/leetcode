# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self.explore(root, 0)

    def explore(self, root, value):
        self.values.add(value)
        if root.left:
            self.explore(root.left, value * 2 + 1)

        if root.right:
            self.explore(root.right, value * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)