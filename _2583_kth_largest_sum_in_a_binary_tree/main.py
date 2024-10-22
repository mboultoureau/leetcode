# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        nodes = deque([root])

        while nodes:
            length = len(nodes)
            value = 0

            for _ in range(length):
                node = nodes.popleft()
                value += node.val

                if node.left:
                    nodes.append(node.left)

                if node.right:
                    nodes.append(node.right)

            heapq.heappush(values, value)

        if len(values) < k:
            return -1

        return heapq.nlargest(k, values)[-1]