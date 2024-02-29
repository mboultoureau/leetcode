# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        level = 0
        previous = 0

        queue = deque([root])
        while queue:
            length = len(queue)
            if level % 2 == 0:
                previous = 0
            else:
                previous = math.inf

            for _ in range(length):
                node = queue.popleft()

                if (node.val % 2 == level % 2 or 
                level % 2 == 0 and node.val <= previous or
                level % 2 == 1 and node.val >= previous):
                    return False

                previous = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1

        return True