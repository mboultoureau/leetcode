# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root.left, root.right])
        
        while len(queue) > 0:
            length = len(queue) // 2
            for _ in range(length):
                left = queue.popleft()
                right = queue.pop()

                if not left and not right:
                    continue

                if not left or not right or left.val != right.val:
                    return False

                queue.appendleft(left.right)
                queue.appendleft(left.left)

                queue.append(right.left)
                queue.append(right.right)

        return True