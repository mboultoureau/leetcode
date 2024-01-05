# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        queue = deque([root])

        while len(queue) > 0:
            length = len(queue)
            row = []

            for _ in range(length):
                first = queue.popleft()
                if first:
                    row.append(first.val)
                    queue.append(first.left)
                    queue.append(first.right)

            if len(row) > 0:
                output.insert(0, row)

        return output