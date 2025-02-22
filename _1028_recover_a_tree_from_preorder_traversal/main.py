# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # Traversal has always one node
        traversal = traversal.split('-')
        
        root = TreeNode(val=int(traversal[0]), left=None, right=None)
        root.parent = None

        self.traverse(traversal, 1, 0, root)

        return root

    def traverse(self, traversal: list, i: int, current_deep: int, root: TreeNode):
        if i >= len(traversal):
            return

        # Get to the correct deep
        deep = 0
        while i < len(traversal):
            if traversal[i] == '':
                i += 1
                deep += 1
            else:
                break

        while current_deep > deep:
            current_deep -= 1
            root = root.parent

        if not root.left:
            root.left = TreeNode(val=int(traversal[i]), left=None, right=None)
            root.left.parent = root
            self.traverse(traversal, i + 1, current_deep + 1, root.left)
        else:
            root.right = TreeNode(val=int(traversal[i]), left=None, right=None)
            root.right.parent = root
            self.traverse(traversal, i + 1, current_deep + 1, root.right)