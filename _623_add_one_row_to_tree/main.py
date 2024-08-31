# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Solution 1
        if depth == 1:
            return TreeNode(val, left=root)

        depth -= 2

        queue = deque([root])
        while queue and depth > 0:
            length = len(queue)
            depth -= 1
            for _ in range(length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        while queue:
            node = queue.popleft()

            newNode = TreeNode(val, left=node.left)
            node.left = newNode

            newNode = TreeNode(val, right=node.right)
            node.right = newNode

        return root
        


        # Solution 2
        # if depth == 1:
        #     newRoot = TreeNode(val=val, left=root, right=None)
        #     return newRoot

        # current = 2
        # queue = deque([root])

        # while queue:
        #     if current == depth:
        #         while queue:
        #             node = queue.popleft()
        #             newNodeLeft = TreeNode(val=val, left=node.left, right=None)
        #             newNodeRight = TreeNode(val=val, left=None, right=node.right)

        #             node.left = newNodeLeft
        #             node.right = newNodeRight

        #         return root
            

        #     length = len(queue)
        #     current += 1
        #     for _ in range(length):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)


