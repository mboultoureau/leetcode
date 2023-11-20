# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Solution 2
        if min(p.val, q.val) <= root.val and max(p.val, q.val) >= root.val:
            return root

        if min(p.val, q.val) < root.val and root.left:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val and root.right:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

        # Solution 1
        # if p.val == root.val or q.val == root.val:
        #     return root

        # if min(p.val, q.val) < root.val and max(p.val, q.val) > root.val:
        #     return root

        # if p.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return self.lowestCommonAncestor(root.right, p, q)
