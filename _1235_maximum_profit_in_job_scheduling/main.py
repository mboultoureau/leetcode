class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # With NeetCode video
        intervals = sorted(zip(startTime, endTime, profit))

        @lru_cache(None)
        def dfs(i):
            if len(intervals) == i:
                return 0

            # don't include i
            result = dfs(i + 1)

            # include i
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            result = max(result, intervals[i][2] + dfs(j))
            return result

        return dfs(0)