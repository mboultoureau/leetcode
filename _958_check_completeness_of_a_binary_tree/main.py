# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        stop = False

        while queue:
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()

                if stop and (node.left or node.right):
                    return False

                if not node.left:
                    if node.right:
                        return False
                    stop = True
                else:
                    queue.append(node.left)
                
                if not node.right:
                    stop = True
                else:
                    queue.append(node.right)

        return True