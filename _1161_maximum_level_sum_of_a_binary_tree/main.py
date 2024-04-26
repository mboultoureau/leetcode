# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        bestLevel = 0
        currentLevel = 0
        bestSum = -math.inf
        currentSum = 0
        queue = deque([root])

        while queue:
            currentLevel += 1
            currentSum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                currentSum += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            if currentSum > bestSum:
                bestSum = currentSum
                bestLevel = currentLevel

        return bestLevel