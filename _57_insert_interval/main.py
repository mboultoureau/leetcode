class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Solution 3
        result = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            elif intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]

        result.append(newInterval)
        return result


        # Solution 2
        # if len(intervals) == 0:
        #     return [newInterval]

        # result = []

        # if intervals[0][0] > newInterval[1]:
        #     result.append(newInterval)

        # i = 0
        # while i < len(intervals):
        #     if i + 1 < len(intervals) and intervals[i][1] < newInterval[0] and intervals[i + 1][0] > newInterval[1]:
        #         result.append([intervals[i][0], intervals[i][1]])
        #         result.append(newInterval)
        #     elif intervals[i][1] < newInterval[0] or intervals[i][0] > newInterval[1]:
        #         result.append([intervals[i][0], intervals[i][1]])
        #     else:
        #         minimum = min(intervals[i][0], newInterval[0])
        #         while i + 1 < len(intervals) and intervals[i + 1][0] <= newInterval[1]:
        #             i += 1
        #         maximum = max(intervals[i][1], newInterval[1])

        #         result.append([minimum, maximum])
        #     i += 1 

        # if intervals[i - 1][1] < newInterval[0]:
        #     result.append(newInterval)

        # return result

        
        # Solution 1
        # # Step 1: insert interval
        # default_len = len(intervals)

        # for i in range(default_len):
        #     if intervals[i][0] > newInterval[0] or (intervals[i][0] == newInterval[0] and intervals[i][0] < newInterval[1]):
        #         intervals.insert(i, newInterval)
        #         break

        # if default_len == len(intervals):
        #     intervals.append(newInterval)

        # # Step 2: merge
        # i = 0
        
        # while i < default_len:
        #     if intervals[i + 1][0] >= intervals[i][0] and intervals[i + 1][0] <= intervals[i][1]:
        #         intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
        #         intervals.pop(i + 1)
        #         default_len -= 1
        #     else:
        #         i += 1

        # return intervals