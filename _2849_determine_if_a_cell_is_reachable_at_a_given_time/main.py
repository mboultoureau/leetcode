class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        distance = max(abs(sx - fx), abs(sy - fy))
        if distance == 0 and t == 1:
            return False

        return distance <= t