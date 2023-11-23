# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        stack = []

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val

            current = current.right

    # Solution 1
    # count = 0
    # answer = 0
    # found = False

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     if self.found:
    #         return self.answer

    #     if not root:
    #         return

    #     self.kthSmallest(root.left, k)
        
    #     if self.found:
    #         return self.answer

    #     self.count += 1

    #     if self.count == k:
    #         self.found = True
    #         self.answer = root.val
    #         return self.answer


    #     self.kthSmallest(root.right, k)

    #     return self.answer