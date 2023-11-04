class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left:
            return n - min(right)
        
        if not right:
            return max(left)

        return max(max(left), n - min(right))

        # Solution 1
        # return max(max(left) if len(left) > 0 else 0, n - min(right) if len(right) > 0 else 0)