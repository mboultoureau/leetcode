# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        bad = n
        left = 1
        right = n

        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                bad = min(bad, middle)
                right = middle - 1
            else:
                left = middle + 1

        return bad