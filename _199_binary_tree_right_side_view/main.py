# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        queue = deque([root])
        while queue:
            last_node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    last_node = node
                    queue.append(node.left)
                    queue.append(node.right)

            if last_node:
                result.append(last_node.val)

        return result