# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Solution 2
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            row = []
            for _ in range(len(queue)):
                root = queue.popleft()
                row.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)

            result.append(row)

        return result


        # Solution 1
        # result = []

        # def order(root: Optional[TreeNode], level):            
        #     if not root:
        #         return

        #     nonlocal result

        #     if len(result) > level:
        #         result[level].append(root.val)
        #     else:
        #         result.append([root.val])

        #     order(root.left, level + 1)
        #     order(root.right, level + 1)
    
        # order(root, 0)

        # return result