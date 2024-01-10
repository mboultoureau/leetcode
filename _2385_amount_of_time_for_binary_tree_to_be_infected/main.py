# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# override
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None, infected=False):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.infected = infected

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Create bidirectionnal graph
        def explore(root, currentHead):
            nonlocal startNode

            if root.left:
                left = Node(root.left.val, None, None, currentHead)
                currentHead.left = left
                explore(root.left, currentHead.left)

            if root.right:
                right = Node(root.right.val, None, None, currentHead)
                currentHead.right = right
                explore(root.right, currentHead.right)

            if currentHead.val == start:
                startNode = currentHead

        startNode = None
        head = Node(root.val, None, None, None)
        explore(root, head)

        startNode.infected = True

        # Propagation
        queue = deque([startNode])
        step = 0

        while len(queue) > 0:
            length = len(queue)
            step += 1

            for i in range(length):
                node = queue.popleft()
                if node.left and not node.left.infected:
                    node.left.infected = True
                    queue.append(node.left)

                if node.right and not node.right.infected:
                    node.right.infected = True
                    queue.append(node.right)

                if node.parent and not node.parent.infected:
                    node.parent.infected = True
                    queue.append(node.parent)

        return step - 1