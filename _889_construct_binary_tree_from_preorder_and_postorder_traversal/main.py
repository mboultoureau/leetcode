# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val=preorder[0], left=None, right=None)
        root.parent = None
        
        self.explore(preorder, postorder, 1, 0, root)

        return root
        
    def explore(self, preorder: List[int], postorder: List[int], preIndex: int, postIndex: int, root: TreeNode):
        if preIndex >= len(preorder):
            return

        if root.val == postorder[postIndex]:
            self.explore(preorder, postorder, preIndex, postIndex + 1, root.parent)
            return

        if root.left:
            root.right = TreeNode(val=preorder[preIndex], left=None, right=None)
            root.right.parent = root
            self.explore(preorder, postorder, preIndex + 1, postIndex, root.right)
        else:
            root.left = TreeNode(val=preorder[preIndex], left=None, right=None)
            root.left.parent = root
            self.explore(preorder, postorder, preIndex + 1, postIndex, root.left)