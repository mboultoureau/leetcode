class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maximum = 0

        for i in range(len(points) - 1):
            if points[i + 1][0] > points[i][0]:
                maximum = max(maximum, points[i + 1][0] - points[i][0])

        return maximum 