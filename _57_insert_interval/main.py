class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Step 1: insert interval
        default_len = len(intervals)

        for i in range(default_len):
            if intervals[i][0] > newInterval[0] or (intervals[i][0] == newInterval[0] and intervals[i][0] < newInterval[1]):
                intervals.insert(i, newInterval)
                break

        if default_len == len(intervals):
            intervals.append(newInterval)

        # Step 2: merge
        i = 0
        
        while i < default_len:
            if intervals[i + 1][0] >= intervals[i][0] and intervals[i + 1][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
                default_len -= 1
            else:
                i += 1

        return intervals