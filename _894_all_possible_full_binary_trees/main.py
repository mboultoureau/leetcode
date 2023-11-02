# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        elif n == 1:
            return [TreeNode(0)]
        else:
            solutions = []
            for nb in range(1, n, 2):
                possibilitiesA = self.allPossibleFBT(nb)
                possibilitiesB = self.allPossibleFBT(n - nb - 1)
                for possA in possibilitiesA:
                    for possB in possibilitiesB:
                        current = TreeNode(0)
                        current.left = possA
                        current.right = possB
                        solutions.append(current)

            return solutions