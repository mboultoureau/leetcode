class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        intervals.sort()
        result.append(intervals[0]) # intervals.length >= 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= result[len(result) - 1][0] and intervals[i][0] <= result[len(result) - 1][1]:
                result[len(result) - 1][1] = max(result[len(result) - 1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result

