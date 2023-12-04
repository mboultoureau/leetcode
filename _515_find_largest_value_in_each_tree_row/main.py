# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            maximum = -math.inf
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                
                maximum = max(maximum, node.val)

            result.append(maximum)

        return result
